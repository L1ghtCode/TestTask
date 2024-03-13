import pandas as pd

def get_pairs(products_df, categories_df):
    """
    Возвращает все пары «Имя продукта – Имя категории» и имена всех продуктов,
    у которых нет категорий.

    :param products_df: DataFrame с продуктами и их категориями.
    :param categories_df: DataFrame с категориями.
    :return: DataFrame с парами "Имя продукта - Имя категории" и именами продуктов без категорий.
    """
    # Объединяем продукты и категории по ключу "category_id" с помощью left join
    merged_df = pd.merge(products_df, categories_df, left_on='category_id', right_on='id', how='left')

    # Выбираем только нужные столбцы: имя продукта и имя категории
    pairs_df = merged_df[['name_x', 'name_y']].rename(columns={'name_x': 'product_name', 'name_y': 'category_name'})

    # Заменяем NaN на "Uncategorized" в столбце category_name
    pairs_df['category_name'].fillna('Uncategorized', inplace=True)

    return pairs_df


# Примеры данных
# Первый дата фрейм без названий категорий
products_data = {"name": ["Куриное филе", "Сыр", "Гречка"], "category_id": [1, 2, None]}
# Второй дата фрейм с названиями категорий
categories_data = {"id": [1, 2], "name": ["Мясо", "Молочная продукция"]}

# Создание DataFrame для продуктов и категорий
products_df = pd.DataFrame(products_data)
categories_df = pd.DataFrame(categories_data)

result = get_pairs(products_df, categories_df)

# Вывод результатов
print(result)

'''
Не работал с PySpark, но задание я понял и решил выполнить его с теми средствами, с которыми работал. 
Надеюсь я смогу изучить PySpark в дальнейшем. Ведь при попытке запустить код, я ловил ошибку порта.
'''
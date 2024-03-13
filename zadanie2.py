import math

class Geometry:
    @staticmethod
    def circle_area(radius):
        return math.pi * radius**2

    @staticmethod
    def triangle_area(side1, side2, side3):
        # Проверка на существование треугольника
        if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
            # По формуле Герона
            s = (side1 + side2 + side3) / 2
            area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
            return area
        else:
            return "Такой треугольник не существует."

    @staticmethod
    def is_right_triangle(side1, side2, side3):
        sides = [side1, side2, side3]
        sides.sort()
        return sides[0]**2 + sides[1]**2 == sides[2]**2

def main():
    while True:
        print("Выберите фигуру для вычисления площади:")
        print("1. Круг")
        print("2. Треугольник")
        print("3. Выйти")
        
        choice = input("Введите номер: ")
        
        if choice == '1':
            radius = float(input("Введите радиус круга: "))
            print("Площадь круга:", Geometry.circle_area(radius))
        elif choice == '2':
            side1 = float(input("Введите длину первой стороны треугольника: "))
            side2 = float(input("Введите длину второй стороны треугольника: "))
            side3 = float(input("Введите длину третьей стороны треугольника: "))
            print("Площадь треугольника:", Geometry.triangle_area(side1, side2, side3))
            print("Является ли треугольник прямоугольным:", Geometry.is_right_triangle(side1, side2, side3))
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте еще раз.")
        print("")
main()

# Создать класс Triangle для представления треугольника. Поля данных должны включать
# углы и стороны. Требуется реализовать операции: получения и изменения полей данных,
# вычисления площади, вычисление периметра, вычисление высот, а также определения вида треугольника
# (равносторонний, равнобедренный или прямоугольный).

import math
class Triangle:

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def __str__(self):
        return (f'Side one: {self.side1}\n'
                f'Side two: {self.side2}\n'
                f'Side three: {self.side3}')

    def set_side_one(self, new_side_one):
        self.side1 = new_side_one
    def set_side_two(self, new_side_two):
        self.side2 = new_side_two
    def set_side_three(self, new_side_three):
        self.side3 = new_side_three
    def get_sides(self):
        return self.side1, self.side2, self.side3

    def count_p(self):
        return self.side1 + self.side2 + self.side3

    def area_triangle(self):
        half_p = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(half_p * (half_p - self.side1) * (half_p - self.side2) * (half_p - self.side3))
        return area

        # return math.sqrt((self.side1 + self.side2 + self.side3) / 2 * \
        #                  ((self.side1 + self.side2 + self.side3) / 2 - self.side1) * \
        #                  ((self.side1 + self.side2 + self.side3) / 2 - self.side2) * \
        #                  ((self.side1 + self.side2 + self.side3) / 2 - self.side3))

# Высота в прямоугольном треугольнике h =  a*b/c
    def height_tr(self):
        return (self.side1 * self.side2) / self.side3

    def type_triangle(self):
        if self.side1 == self.side2 and self.side1 == self.side3 and self.side2 == self.side3:
            return ('Треугольник равносторонний')
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return ('Треугольник равнобедренный')
        else:
            return ('Треугольник прямоугольный')


triangle = Triangle(3, 3, 3)
print(triangle)

print('------------------')

triangle.set_side_one(5)
triangle.set_side_two(6)
triangle.set_side_three(7)
print(triangle.get_sides())
print(triangle)

print('------------------')

print(triangle.count_p())

print(triangle.area_triangle())

print(triangle.height_tr())

print(triangle.type_triangle())

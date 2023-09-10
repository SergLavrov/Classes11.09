# Создать класс Money для работы с денежными суммами. Число должно быть представлено
# двумя полями: типа long для рублей и типа unsigned char — для копеек.
# Дробная часть (копейки) при выводе на экран должна быть отделена от целой части запятой.
# Реализовать сложение, вычитание, деление сумм, деление суммы на дробное число,
# умножение на дробное число и операции сравнения.

class Money:
    def __init__(self, long1, unsigned_char1, long2, unsigned_char2,):
        self.long1 = long1
        self.unsignedChar1 = unsigned_char1
        self.long2 = long2
        self.unsignedChar2 = unsigned_char2

    def __str__(self):
        return (f'{self.long1},{self.unsignedChar1}\n'
                f'{self.long2},{self.unsignedChar2}')

    def summ(self):
        longs = self.long1 + self.long2
        chars = self.unsignedChar1 + self.unsignedChar2
        if chars > 100:
            return (f'{longs + 1},{chars % 100 // 10}{chars % 10}')
        else:
            return (f'{longs},{chars}')

    def minus(self):
        longs = self.long1 - self.long2
        chars = self.unsignedChar1 - self.unsignedChar2
        if self.unsignedChar1 < self.unsignedChar2:
            chars = self.unsignedChar1 * 10 - self.unsignedChar2
            return (f'{longs - 1},{chars}')
        else:
            return (f'{longs},{chars}')

money = Money(30, 10, 25, 15)
print(money)

print(money.summ())

print(money.minus())

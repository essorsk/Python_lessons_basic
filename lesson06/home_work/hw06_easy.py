# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

#Задаем ф-цию длинны стороны
def side_len(a,b):
    return math.sqrt(((b[0] - a[0]) ** 2) + ((b[1] - a[1]) ** 2))


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.ab = side_len(self.a, self.b)
        self.bc = side_len(self.b, self.c)
        self.ac = side_len(self.a, self.c)


    def perim(self):
        return round((self.ab + self.ac + self.bc), 1)


    def height(self, side):
        ab = self.ab
        bc = self.bc
        ac = self.ac
        hlf = self.perim() / 2
        return round(((2 / side) * math.sqrt(hlf * (hlf - ab) * (hlf - bc) * (hlf - ac))),1)

    #Определение высоты из всех точек треугольника

    def height_a(self):
        return round(self.height(self.bc), 1)


    def height_b(self):
        return round(self.height(self.ac), 1)


    def height_c(self):
        return round(self.height(self.ab), 1)

    def sq(self):
        return round(((self.ac / 2) * self.height_b()), 1)


t1 = Triangle((0,1), (4,7), (9,1))
print('\nTriangle is:\n Perimetr: ', t1.perim())
print(' Height: ', t1.height_b())
print(' Square: ', t1.sq())
        


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezz:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.ab = round(side_len(self.a, self.b), 1)
        self.bc = round(side_len(self.b, self.c), 1)
        self.cd = round(side_len(self.c, self.d), 1)
        self.ad = round(side_len(self.a, self.d), 1)

    def check(self):
        return side_len(self.c, self.a) == side_len(self.b, self.d)


    def perimeter(self):
        return round((self.ab + self.bc + self.cd + self.ad),1)

    def square(self):
        return round(((self.ad + self.bc)/4) * math.sqrt((4 * (self.ab ** 2)) - ((self.ad - self.bc) ** 2)),1)
    
tr1 = Trapezz((0, 0), (2, 1), (2, 3), (0, 4))
print('\nGiven figure:')
print('Have sides: {}, {}, {}, {}.'.format(tr1.ab, tr1.bc, tr1.cd, tr1.ad))
print('If figure right trapezia: ', tr1.check())
print('Perimetr is: ', tr1.perimeter())
print('Square is: ', tr1.square())


    


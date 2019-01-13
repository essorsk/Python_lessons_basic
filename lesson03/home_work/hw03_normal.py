__author__ = 'Козина Светлана Владимировна'
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
print('\nЗадание-1: Fibonacci')
#M = (M-1)+(M-2)
def fibonacci(n, m):
    a = 1
    b = 1

    for i in range(3, m + 1):
        b += a
        a, b = b, a
        if i >= n:
            print(a)

n = int((input('Введите позицию начала цикла: ')))
m = int((input('Введите позицию конца цикла: ')))
fibonacci(n, m)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

print('\nЗадача-2: Sort')
def sort_to_max(origin_list):
    
    for i in range(1, len(origin_list)):
        cle = origin_list[i]
        k = i - 1
        while k >= 0 and cle < origin_list[k]:
            origin_list[k + 1] = origin_list[k]
            k -= 1
            origin_list[k + 1] = cle
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
print('\nЗадача-3: Filter')
def craft_filter(cond,list):
    craft = []
    for i in list:
        if i != cond:
            craft.append(i)
    print(craft)

# Genetate random list to check filter
import random
n = 30
rlist = []
i = 0
while i < n:
    rlist.append(random.randint(-10,20))
    i += 1
print('Исходные данные: ', rlist)
f = int(input('Определите, что отфильтровать: '))
craft_filter(f,rlist)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

print('\nЗадача-4: Geometry')
def edge(x1,x2,y1,y2):
    ed = ((x2-x1)**2+(y2-y1)**2)**(1/2)
    return ed
def angl(x1,x2,y1,y2):
    an = (y1-y2)/(x1-x2)
    return an
print('Введите координаты искомой фигуры: ')
x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))
x3 = int(input('x3: '))
y3 = int(input('y3: '))
x4 = int(input('x4: '))
y4 = int(input('y4: '))
if edge(x1,x2,y1,y2) == edge(x3,x4,y3,y4) and angl(x1,x2,y1,y2) == angl(x3,x4,y3,y4):
    print('Это параллелограмм')
else:
    print('Эта фигура нечто иное')


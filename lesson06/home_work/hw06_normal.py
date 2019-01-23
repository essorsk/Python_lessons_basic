# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Teacher:
    def __init__(self, surname, course):
        self.surname = surname
        self.course = course

class ClassRoom:
    def __init__(self, number, teachers):
        self.number = number
        self.teachers = teachers

class Student:
    def __init__(self, name, surname, mother, father, class_room):
        self.name = name
        self.surname = surname
        self.mother = mother
        self.father = father
        self.class_room = class_room

teachers = {
    'Ложкин': Teacher('Ложкин', 'Математика'),
    'Поварежкин': Teacher('Поварежкин', 'Русский'),
    'Вилкин': Teacher('Вилкин', 'История'),
    'Указкин': Teacher('Указкин', 'Физ-ра'),
    'Рояль': Teacher('Рояль', 'Музыка'),
}

classes = {
    '5А': ClassRoom('5А', ['Ложкин', 'Вилкин', 'Рояль']),
    '6Б': ClassRoom('6Б', ['Указкин', 'Поварежкин']),
    '2Г': ClassRoom('2Г', ['Ложкин', 'Указкин']),
    '3В': ClassRoom('3В', ['Рояль', 'Ложкин', 'Поварежкин']),
}

students = {
   'Семен Конев': Student('Семен', 'Конев', 'Конева Татьяна', 'Конев Олег', '5А'),
   'Игорь Конев': Student('Игорь', 'Конев', 'Конева Татьяна', 'Конев Олег', '3В'),
   'Анна Алексеева': Student('Анна', 'Алексеева', 'Алексеева Татьяна', 'Алексеев Вадим', '6Б'),
   'Василий Ким': Student('Василий', 'Ким', 'Ким Наталья', 'Ким Иван', '2Г'),
   'Матвей Юлин': Student('Матвей', 'Юлин', 'Юлина Евгения', 'Юлин Пётр', '3В'),
}

print('1. Полный список всех классов школы: ')
for el in classes:
    print(el)


#  (каждый ученик отображается в формате "Фамилия И.О.")
class_room = '3В'
print('\n Cписок всех учеников в указанном классе: ', class_room)
for el in students.values():
    if el.class_room == class_room:
        print(el.name, el.surname)


#  (Ученик --> Класс --> Учителя --> Предметы)

fullname = 'Семен Конев'
print('\n Cписок всех предметов указанного ученика: ', fullname)
if fullname in students:
    class_room = students[fullname].class_room
    if class_room in classes:
        for surname in classes[class_room].teachers:
            if surname in teachers:
                print(teachers[surname].course)


fullname = 'Василий Ким'
print('ФИО родителей указанного ученика: ', fullname)
if fullname in students:
    print('Мать: ', students[fullname].mother)
    print('Отец: ', students[fullname].father)


class_room = '6Б'
print('\n Cписок всех Учителей, преподающих в указанном классе: ', class_room)
if class_room in classes:
    print(classes[class_room].teachers)

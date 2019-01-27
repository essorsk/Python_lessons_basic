#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""


import random

#Sort ascending in rows
def sort_up(rough_list, begin, end):
    for i in range(end, begin, -1):
        for j in range(begin, i):
            if rough_list[j] > rough_list[j + 1]:
                rough_list[j], rough_list[j + 1] = rough_list[j + 1], rough_list[j]


#Generator of loto Cards
class Card():
    def __init__(self):
        self._row_count = 3
        self._column_count = 9
        self._nir_count = 5  #number in row
        self._numbers = random.sample(range(1, 91), 15)
        self._kegs_count = 15
        self._distr_row = list()

        for i in range (self._row_count):
            sort_up(self._numbers, self._nir_count * i, self._nir_count * (i+1)-1)
            self._distr_row += random.sample(range(self._column_count), self._nir_count)

    def __str__(self):
        card = ''
        num_index = 0
        for row in range(self._row_count):
            for cl in range(self._column_count):
                if cl in self._distr_row[self._nir_count * row: self._nir_count * (row + 1)]:
                    card += ' ' *(2 - len(str(self._numbers[num_index]))) + str(self._numbers[num_index]) + ' '
                    num_index += 1
                else:
                    card += ' ' * 3
            card += '\n'
        return card

    def delete_nums(self, keg):
        i = self._numbers.index(keg)
        self._numbers[i] = '-'
        self._kegs_count -= 1
        return True


#Game body
my_card = Card()
c_card = Card()
print('***  Welcome to LOTO!  ***\n')
kegs = random.sample(range(1, 91), 90)
step = 0
do = ''
while my_card._kegs_count  > 0 and c_card._kegs_count > 0 and do != 'q':
    print('\nCurrent nimber is  |{}|  (remain {})'.format(kegs[step], 90 - step - 1))
    print('\n------- Your Card  -------')
    print(my_card)
    print('-----  Computer Card  -----')
    print(c_card)
    do = input('Do you want to close your number?  (y/n/q):  ')

    try:
        bingo = my_card.delete_nums(kegs[step])
    except ValueError:
        bingo = False

    try:
        c_card.delete_nums(kegs[step])
    except ValueError:
        pass

    if (do == 'y' and not bingo) or (do == 'n' and bingo):
        print('Sorry, you loose. Wrong choice ;(')
        do = 'q'
    if do != 'y' and do != 'n' and do != 'q':
        print ('Wrong command, try new game...')
        do = 'q'
    print()
    step +=1

if my_card._kegs_count == 0:
    print('You win!!!')
elif c_card._kegs_count == 0:
    print('You loose ;(')
elif my_card._kegs_count == 0 and c_card._kegs_count == 0:
    print('Win-Win!')




















                    

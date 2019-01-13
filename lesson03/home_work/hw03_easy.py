
__author__ = 'Козина Светлана Владимировна'
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
print('\nЗадание-1: round')
def my_round(number, ndigits):
    convert = number * (10 ** ndigits)
    dot = len(str(int(convert))) + 1
    if int(str(convert)[dot]) > 5:
        convert += 1
    return float(int(convert) / (10 ** ndigits))


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    digs = [int(i) for i in str(ticket_number)]
    if len(digs) != 6:
        return False
    head = sum(digs[:3])
    tale = sum(digs[3:])
    if head == tale:
        return True
    else:
        return False

print('\nЗадание-2: Lucky ticket')
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number = number*(10**ndigits) + 0.41
    number = number // 1
    number = number / (10**ndigits)
    return number


print(my_round(2.1234567, 5)) # 2.12346
print(my_round(2.1999967, 5)) # 2.2
print(my_round(2.9999967, 5)) # 3.0



# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
'''

def lucky_ticket(ticket_number):
    num = str(ticket_number)
    l1 = int(num[:1]) + int(num[1:2])
    l2 = int(num[-1]) + int(num[-2])
    if l1 == l2:
        return True
    else:
        return False
    
'''
lucky_ticket = lambda x : (lambda x : 'Счастливый билет' if sum(x[:3]) == sum(x[3:]) else 'Лучше взять другой билет')(list(map(int, list(str(x)))))

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

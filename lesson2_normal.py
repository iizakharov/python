# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math

list1 = [2, -5, 8, 9, -25, 25, 4]
new_list = []
for i in list1:
    if i > 0 and (math.sqrt(i)) % 1==0:
        i = math.sqrt(i)
        new_list.append(int(i))
print(new_list)


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)


date = '03.09.2018'
list_d = date.split('.')
base_d = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвёртое', '05': 'пятое', '06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое', '11': 'одиннадцатое', '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое', '21': 'двадцать первое', '22': 'двадцать второе', '23': 'двадцать третье', '24': 'двадцать четвёртое', '25': 'двадцать пятое', '26': 'двадцать шестое', '27': 'двадцать седьмое', '28': 'двадцать восьмое', '29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое'}
base_m = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля','05': 'мая','06': 'июня', '07': 'июля', '08': 'августа','09': 'сентября', '10': 'октября','11': 'ноября', '12': 'декабря'}
for a in base_d:
    if list_d[0] == a:
        list_d[0] = base_d[a]
for a in base_m:
    if list_d[1] == a:
        list_d[1] = base_m[a]
new_date = list_d[0] + ' ' + list_d[1] + ' '+ list_d[2]+ ' года'
print(new_date)


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random

list_n = []
for n in (random.randint(-100, 100)): #не работает
    list_a.append(n)
print(list_n)    


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

list_41 = [1, 2, 4, 5, 6, 2, 5, 2]
list_42 = set(list_41)
print(list_42)

list_43 = []
for l in list_41:
  if list_41.count(l) == 1:
    list_43.append(l)
print(list_43)


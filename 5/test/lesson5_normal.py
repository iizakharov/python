# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os, sys
import lesson5_easy as easy
print('sys.argv = ', sys.argv)
print('\n \n Добро пожаловать в консольную утилиту!')

arg = '_'
while arg!= '0':
    print('\n \n МЕНЮ:')
    print('1 - Перейти в папку')
    print('2 - Посмотреть содержимое текущей папки')
    print('3 - Удалить папку')
    print('4 - Создать папку')
    print('0 - Выйти')
    arg = input("Что делаем? 1/2/3/4/0:   ")
    print(arg)
    if arg == '1':
        path = input('Введите полный адрес директории: ')
        os.chdir(path)
        print('Теперь мы в', path)
    elif arg == '2':
        path = os.getcwd()
        easy.list_dir(path)
    elif arg == '3':
        namedir = input('Введите имя директории для удаления: ')
        easy.del_dir(namedir)
    elif arg == '4':
        namedir = input('Введите имя будущей директории: ')
        easy.make_dir(namedir)
    elif arg == '0':
        pass
    else:
        print('Нет такого пункта!')

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os, sys, shutil


#Скрипт создания директорий

path = os.path.join(os.getcwd())
def make_dirs(name):
    my_dirs = os.path.join(os.getcwd(), name)
    for i in range(1, 10):
        try:
            os.mkdir(my_dirs +str(i))
        except FileExistsError:
            print('Такая директория уже существует')
        else:
            print("Успешно создана директория ")

#Скрипт создания одной директории

def make_dir(name):
    my_dir = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(my_dir)
    except FileExistsError:
        print('Такая директория уже существует')
    else:
        print("Успешно создана директория ")

#Скрипт удаления этих же директорий

def del_dirs(name):
    d_dirs = os.path.join(os.getcwd(), name)
    for i in range(1, 10):
        try:
            os.rmdir(d_dirs +str(i))
        except FileExistsError:
            print('Такой директории не существует')
        else:
            print("Успешно удалено ")
            
# Скрипт удаляющий только заданную директорию

def del_dir(name):
    name = os.path.join(os.getcwd(), name)
    try:
        os.rmdir(name)
    except FileExistsError:
        print('Такой директории не существует')
    else:
        print("Успешно удалено ")

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir(path):
    
    for _ in os.listdir(path):
        print(_)
path = os.getcwd()
    

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file(first, second):
    shutil.copy(first, second)
    #first = sys.argv[0]
    #secont = first + '.py'

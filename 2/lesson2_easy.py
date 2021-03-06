# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fr_rus = ["Яблоки", "Банан", "Киви", "Арбуз"]
i = 0
n = 1

for i in fr_rus:
    print(str(n) +'.  ' + str(i))
    n += 1
    
#Вариант 2:

frut = ["Яблоки", "Банан", "Киви", "Арбуз"]
i = 0
for a in frut:
    i +=1
    print(f"{i}.  {a}")



# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

first = [2, 3, 4, 5, 6, 7, 8, 9]
second = [1, 2, 9, 4, 25]
for a in first:
  if a in second:
    first.remove(a)
print(first)



# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

list1 = [2, 3, 4, 5, 6, 7, 8, 9]
new_list = []
for i in list1:
    if i % 2 == 0:
      i /= 4
    else:
      i *= 2
    new_list.append(i)
print(new_list)



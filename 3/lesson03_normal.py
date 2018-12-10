# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711

def fibanacci(n, m):
  listM = []

  a = 0
  b = 1
  c = 0

  for i in range(m):
    if c < m:
      a, b = b, a + b
      listM.append(a)
    c += 1
  print(listM[n-1:]) 
  

n = int(input('Введите номер первого элемента списка Фибоначи: '))
m = int(input('Номер последнего элемента Фибоначи: '))

fibanacci(n, m)




# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    
    n = 1
    while n < len(origin_list):
        for i in range(len(origin_list)-n):
            if origin_list[i] > origin_list[i+1]:
                origin_list[i], origin_list[i+1] = origin_list[i+1], origin_list[i]
        n +=1
    print('\n Ответ задачи 2: ')   
    print(origin_list)

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

print('\n Задача-3: ')
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filt(list):
    
    for i in list:
        if i == 0: 
            list.remove(i)
        elif i == '':
            list.remove(i)
        elif i <= 0:
            list.remove(i)
    print(list)
    

my_filt([2, 10, -12, 'Quest', 2.5, '',20, -11, 4, 4, 0])


print('\n Задача-4: ')
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def f(A1,A2,A3,A4):
  
  if A1[0]+A2[0] == A3[0]+A4[0] and A1[1]+A2[1] == A3[1]+A4[1]:
    print('Точки заданы верно!')
  elif A3[0] +A2[0] == A1[0]+A4[0] and A3[1] +A2[1] == A1[1]+A4[1]:
    print('Точки заданы верно!')
  elif A2[0] +A4[0] == A1[0]+A3[0] and A2[1] +A4[1] == A1[1]+A3[1]:
    print('Точки заданы верно!')
  else:
    print('Ошибка! Задайте другие точки!')

A1 = [2, 1]
A2 = [3, 7]
A3 = [11, 7]
A4 = [10, 1]

f(A1,A2,A3,A4)


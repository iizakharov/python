import math

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))
D = b**2 - (4*a*c)
print("Дискриминант равен: ", D)
if D > 0:
  print("Ответа два!")
  x1 = -b + (math.sqrt(b**2 - 4*a*c))
  x2 = -b - (math.sqrt(b**2 - 4*a*c))
  print("Ответа первый: ", x1)
  print("Ответа второй: ", x2)
elif D == 0:
  x = -b/2*a
  print("Ответа: ", x)
elif D < 0:
  print("Нет действительных корней :( ")



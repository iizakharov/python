# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class treugol:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
    #вычисление днинны стороны по координатам    
        def dlin_stor(a, b):
            return math.sqrt((a[0] -b[0])**2 +(a[1] - b[1])**2)           
        self.AB = dlin_stor(self.A, self.B)
        self.BC = dlin_stor(self.B, self.C)
        self.CA = dlin_stor(self.C, self.A)
    #пириметр
    def perimetr(self):
        return self.AB + self.BC + self.CA
    #полупириметр
    def pol_p(self):
        return self.perimetr()/2
    
    #Находим площадь по формуле Герона
    def plosh(self):
        return math.sqrt(self.pol_p()*(self.pol_p() - self.AB)*(self.pol_p() - self.BC)*(self.pol_p() - self.CA))
    #Высота
    def height(self):
        return self.plosh()*2/self.AB

''' проверка
treugolnik1 = treugol((1, 1), (-2, 4), (-2, -2))
 
print(treugolnik1.plosh())
print(treugolnik1.height())
print(treugolnik1.perimetr())
'''

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math

class Trapecia:
    def __init__(self, A, B, C, D):
               
    #вычисление днинны оснований по координатам    
        def dlin_storon(a,b):
            return math.sqrt((a[0] -b[0])**2 +(a[1] - b[1])**2)
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.AB = dlin_storon(self.A, self.B)
        self.BC = dlin_storon(self.B, self.C)
        self.CD = dlin_storon(self.C, self.D)
        self.DA = dlin_storon(self.D, self.A)

        def perimetr(a,b,c,d):
            return self.AB + self.BC + self.CD + self.DA
    # рассморим равнобедренную трапецию как два одинковых треугольника, тогда
    # также назначим диагонали AC и BD
        self.AC = dlin_storon(self.A, self.C)
        self.BD = dlin_storon(self.B, self.D)
        
        def plosh_triug(a, b, c):
            polu_per = (a+b+c)/2
            return math.sqrt(polu_per*(polu_per-a)*(polu_per-b)*(polu_per-c))

        def ploshad_trap(A,B,C,D):
                return plosh_triug(self.AB, self.BD, self.DA)+plosh_triug(self.BC, self.CD, self,BD)

        def RVBtrap(self):
            if self.AC == self.BD:
                print('Это равнобедренная трапеция')
            else:
                print('Это НЕ! равнобедренная трапеция')

trapecia1 = Trapecia((3, 1), (5, 5), (10, 5),(12,1)) 
 


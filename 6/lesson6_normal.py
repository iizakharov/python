# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class People:
    def __init__(self, surname, name, patronymic):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
 
    def get_full_name(self):
        return self.surname + ' ' + self.name + ' ' + self.patronymic
 
    def get_short_name(self):
        return '{} {}.{}.'.format(self.surname.title(), self.name[0].upper(), self.patronymic[0].upper())


#people1 = People('Иван', 'Иванович', 'Иванов')
#print(people1.get_full_name())
#print(people1.get_short_name())

class Student(People):
    def __init__(self, surname, name, patronymic, mom, dad, school_class):
        People.__init__(self, name, patronymic, surname)
        self.mom = mom
        self.dad = dad
        self.school_class = school_class


class Teacher(People):
    def __init__(self, surname, name, patronymic, subject):
        People.__init__(self, name, patronymic, surname)
        self.subject = subject
 
 
class Class_rooms:
    def __init__(self, class_room, teachers):
        self.class_room = class_room
        self.teachersdict = {t.subject: t for t in teachers}


if __name__ == '__main__':
    teachers = [Teacher('Иванов', 'Иван', 'Иванович', 'Математика'),
                Teacher('Пушкин', 'Александр', 'Сергеевич', 'Литература'),
                Teacher('Орлова', 'Ольга', 'Николаевна', 'Химия'),
                Teacher('Дмитриев', 'Дмитрий', 'Дмитриевич', 'Информатика'),
                Teacher('Васильев', 'Василий', 'Васильевич', 'Физкультура')]
    classes = [Class_rooms('11 А', [teachers[0], teachers[1], teachers[2]]),
               Class_rooms('11 Б', [teachers[1], teachers[3], teachers[4]]),
               Class_rooms('10 А', [teachers[3], teachers[1], teachers[0]])]
    parents = [People('Владимир', 'Владимирович', 'Путин'),
               People('Алина', 'Алексеевна', 'Кабаева'),
               People('Дмитрий', 'Анатольевич', 'Медведев'),
               People('Римма', 'Дмиртриевна', 'Романова'),
               People('Сергей', 'Сергеевич', 'Сергеев'),
               People('Ирина', 'Юрьевна', 'Сергеева')]
    students = [Student('Александр', 'Владимирович', 'Путин', parents[0], parents[1], classes[0]),
                Student('Ольга', 'Дмитриевна', 'Медведева', parents[2], parents[3], classes[1]),
                Student('Андрей', 'Сергеевич', 'Сергеев', parents[4], parents[5], classes[2])]
    print('Список классов в школе: ')
    for f in classes:
        print(f.class_room)
 
    for f in classes:
        print('Учителя, преподающие в {} классе:'.format(f.class_room))
        for teacher in classes[0].teachersdict.values():
            print(teacher.get_full_name())
    for f in classes:
        print("Ученики в {} классе :".format(f.class_room))
        for st in students:
            print(st.get_short_name())
 
    for f in students:
        print('Список предметов ученика {}'.format(f.school_class))
        for teacher in classes[0].teachersdict.values():
            print(teacher.get_full_name())

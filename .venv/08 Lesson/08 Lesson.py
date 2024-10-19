"""
Задача 1: Дана строка. Напишите программу, которая подсчитывает количество вхождений каждого слова в этой строке,
используя словарь.
Пример:
text = "apple orange apple banana orange apple"
Ожидаемый результат:
{'apple': 3, 'orange': 2, 'banana': 1}
Задача 2: Создайте словарь, который будет хранить информацию о студентах. В качестве ключа используйте имя студента,
а в качестве значения — вложенный словарь, содержащий возраст и оценки студента по предметам.
Пример:
Добавьте информацию о нескольких студентах.Найдите средний балл одного из студентов
Задача 3: Оценка посещаемости студентовУсловие: Найдите студентов, посещающих все три предмета, хотя бы два предмета,
и студентов, которые посещают только один предмет.
Вводные данные: Множества студентов по каждому предмету
math_students = {"Alice", "Bob", "Charlie", "David"}
cs_students = {"Bob", "Charlie", "Eve"}
physics_students = {"Charlie", "David", "Eve", "Frank"}
Задача 4: Даны два списка с числами. Напишите программу, которая находит все уникальные числа, присутствующие хотя
бы в одном из списков, и выводит только те из них, которые делятся на 3.
"""
myText = input('Enter fruits: ')
#создаем переменную myList в нее записываем данные из переменной myText при этом разбивая ее с помощью функции split на отдельные элементы
myList = myText.split()
print(myList)
#создаем переменную типа словарь - пустой в ктр мы потом будем записывать данные
myDict = {}
#объявляем цикл в котором мы будем работать с каждым элементом нашего списка
for i in myList:
    #в словаре myDict мы создаем мы создаем новый ключь с именем i т.е. с первым элементом нашего мписка
    #и присваиваем ему значение в которое мы записываем количество элементов i в списке myList
    myDict[i] = myList.count(i)
print(myDict)

dictStudents = {}
students = int(input('How many students do we have? '))
for i in range(students):
    name = input('Student Name: ')
    age = int(input('Student s age: '))
    dictSubjects = {}
    subject = int(input('How many subjects do you have? '))
    for a in range(subject):
        subj = input('Enter subject: ')
        mark = int(input('Enter mark: '))
        dictSubjects[subj] = mark
    #создаем ключь и присваиваем ему значение вот от сюда age = input('Student s age: ')
    dictStudents[name] = {'age': age, 'subject': dictSubjects}
studentName = input('Whom we are looking for? ')
if studentName in dictStudents:
    grades = dictStudents[studentName]['subject'].values()
    average = sum(grades)/len(grades)
print(f'Average grade of student {studentName}) is ', average)


math_students = {"Alice", "Bob", "Charlie", "David"}
cs_students = {"Bob", "Charlie", "Eve"}
physics_students = {"Charlie", "David", "Eve", "Frank"}
#создаем список словарей
subjects = [math_students,cs_students , physics_students]
#обединение множеств
allStudents = math_students.union(cs_students).union(physics_students)
stat = {}
for i in allStudents: #в этом цикле проверяем каждого студента
    count = 0
    for k in subjects: #в этом цикле заходим в словари с предметами и првнряем есть ли там наш студент
        if i in k:
            count += 1
    print('Student ', i, 'attends ', count, ' classes')
    if count not in stat:
        stat[count] = 1
    else:
        stat[count] += 1
for i, k in stat.items():
    print('Number of students who attends ', i, ' classes: ', k)
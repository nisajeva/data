"""
Открытие и чтение файла:
Напишите программу, которая открывает текстовый файл
sample.txt и выводит его содержимое на экран.
"""
with open('Test.txt', 'r') as myFile:
    print(myFile.read())

myFile = open('Test.txt', 'r')
print(myFile.read())
myFile.close()
"""
Запись в файл: Напишите программу, которая создает новый текстовый файл output.txt
и записывает в него строку "Hello, World!".
"""
with open('output.txt', 'w') as myFile:
    myFile.write('Hello, World!')
"""
Создание файла с числовыми данными: Напишите программу, которая создает файл
numbers.txt и записывает в него числа от 1 до 5, каждое на новой строке.
"""
myList = []
with open('numbers.txt', 'w+') as myFile: #w+  тут пишется только для того чтобы распечать и посмотреть, но напрактике лучше использовать W
    x = int(input("Count of numbers "))
    for i in range(x):
        myList.append(i+1)
    for i in myList:
        print(i, file = myFile)
    myFile.seek(0)
    print(myFile.read())
"""
Добавление данных в файл: Напишите программу, которая открывает файл output.txt в
режиме добавления и записывает в него строку "Appending this line.".
"""
with open('output.txt', 'a') as myFile: #a  это как append
    myFile.write('Appending this line\n')
"""
Подсчет строк в файле: Напишите программу, которая открывает файл sample.txt и
подсчитывает количество строк в этом файле.
"""
with open('sample.txt', 'r') as myFile:
    print('sample.txt contains ', len(myFile.readlines()), ' lines')
"""
Чтение и запись файлов: Напишите программу, которая открывает файл input.txt,
читает его содержимое, затем создает новый файл copy.txt и записывает туда
прочитанные данные.
"""
with open('input.txt', 'r') as file1:
    content = file1.read()
    with open('copyInput.tst', 'w') as file2:
        file2.write(content)
"""
Чтение файла и вывод конкретных строк: Напишите программу, которая открывает файл
data.txt и выводит только те строки, которые содержат слово "Python".
"""
with open('data.txt', 'r') as file1:
    data = file1.readlines()
for i in data:
    if 'Python' in i:
        print(i)
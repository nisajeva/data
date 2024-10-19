#1
maximum = max(3, 7, 5)
print("Max number:", maximum)

#3
number = 15
if number % 3 == 0:
    print("Делится")
else:
    print("Не делится")

#4
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

print("Выберите операцию:")
print("1. Сложение (+)")
print("2. Вычитание (-)")
print("3. Умножение (*)")
print("4. Деление (/)")

operation = input("Введите номер операции (1/2/3/4): ")

if operation == '1':
    result = num1 + num2
    print(f"Результат: {num1} + {num2} = {result}")
elif operation == '2':
    result = num1 - num2
    print(f"Результат: {num1} - {num2} = {result}")
elif operation == '3':
    result = num1 * num2
    print(f"Результат: {num1} * {num2} = {result}")
elif operation == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"Результат: {num1} / {num2} = {result}")
    else:
        print("Ошибка: Деление на ноль!")
else:
    print("Некорректный выбор операции.")
#5
numbers = [4, 7, 1, 9, 2]
min = numbers[0]
max = numbers[0]

for number in numbers:
    if number < min:
        min = number
    if number > max:
        max = number
print(f"Min number: {min num}")
print(f"Max number: {max num}")
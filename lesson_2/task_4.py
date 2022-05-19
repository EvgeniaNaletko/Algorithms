"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""

def func(circle, result, number):
    if circle == value:
        return f'Количество элементов: {value}\nИх сумма: {result}'
    else:
        circle += 1
        number = - number / 2
        result += number
        return func(circle, result, number)


result, circle, number = 1, 1, 1
try:
    value = int(input('Введите количество элементов: '))
    print(func(circle, result, number))
except ValueError:
    print('Вы ввели строку.')

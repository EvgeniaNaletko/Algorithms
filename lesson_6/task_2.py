"""
Задание 2.
Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.
Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.
Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import profile

'''
Профилирование рекурсии выдает много таблиц. Чтобы этого не было нужно обернуть функцию
'''

# До
@profile()
def func(number, even_number, odd_number):
    if not number:
        return f'Четных: {even_number}, Нечетных: {odd_number}'
    else:
        if number % 10 % 2 == 1:
            odd_number += 1
        else:
            even_number += 1
        return func(number // 10, even_number, odd_number)

even_number = 0
odd_number = 0
number = int(input('Введите число: '))
print(func(number, even_number, odd_number))

# После
@profile()
def wrapper(num: int):
    def func(number, even_number=0, odd_number=0):
        if not number:
            return f'Четных: {even_number}, Нечетных: {odd_number}'
        else:
            if number % 10 % 2 == 1:
                odd_number += 1
            else:
                even_number += 1
            return func(number // 10, even_number, odd_number)
    return func(num)

print(wrapper(int(input('Введите число: '))))
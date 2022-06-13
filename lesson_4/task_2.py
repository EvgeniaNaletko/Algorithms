"""
Задание 2.
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections
defaultdict(list)
int(, 16)
reduce
2) через ООП
вспомните про перегрузку методов
__mul__
__add__
"""
from collections import defaultdict

nums = defaultdict(list)

first = input('Введите первое число: ')
second = input('Введите второе число: ')
nums[first] = list(first)
nums[second] = list(second)

summ = list(hex(int(''.join(nums[first]), 16) + int(''.join(nums[second]), 16))[2:].upper())
multiplication = list(hex(int(''.join(nums[first]), 16) * int(''.join(nums[second]), 16))[2:].upper())

print(nums)
print(f'Сумма чисел: {summ}')
print(f'Произведение чисел: {multiplication}')
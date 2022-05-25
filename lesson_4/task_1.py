"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import timeit

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

# Небольшое ускорение было достигнуто за счет использования comprehensions
def func_2(nums):
    new_arr = []
    [new_arr.append(i) for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


my_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(func_1(my_arr))
print(timeit('func_1(my_arr)', globals=globals(), number=1000000))

print(func_2(my_arr))
print(timeit('func_2(my_arr)', globals=globals(), number=1000000))


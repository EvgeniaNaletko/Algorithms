"""
Задание 2. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные по длине части:
в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
Решите задачу тремя способами:
3) с помощью встроенной функции поиска медианы сделайте замеры на массивах длиной 10, 100, 1000 элементов
В конце сделайте аналитику какой трех из способов оказался эффективнее
"""
from random import randint
from timeit import timeit
import statistics

def gen_list(m=10):
    my_list = [randint(-100, 100) for i in range(m * 2 + 1)]
    return my_list

def get_median(list_numbers):
    median = statistics.median(list_numbers)
    return f'Вы ввели: {list_numbers}\nМедиана: {median}\n'

#print(get_median(gen_list(5)))
#print(get_median(gen_list()))

print('Время исполнения для массива длиной 10 элементов:')
print(timeit("get_median(gen_list()[:])", globals=globals(), number=100))
print('Время исполнения для массива длиной 100 элементов:')
print(timeit("get_median(gen_list(100)[:])", globals=globals(), number=100))
print('Время исполнения для массива длиной 1000 элементов:')
print(timeit("get_median(gen_list(1000)[:])", globals=globals(), number=100))

"""
Время исполнения для массива длиной 10 элементов:
0.0019295000000000007
Время исполнения для массива длиной 100 элементов:
0.01670490000000001
Время исполнения для массива длиной 1000 элементов:
0.15954020000000002
"""

'''
Вывод: Самым быстрым оказался третий способ (встроенная функция), самым медленным - первый (сортировка). 
'''
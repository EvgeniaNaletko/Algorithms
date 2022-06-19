"""
Задание 2. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные по длине части:
в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
Решите задачу тремя способами:
2) без сортировки
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit

def gen_list(m=10):
    my_list = [randint(-100, 100) for i in range(m * 2 + 1)]
    return my_list

def get_median(list_numbers: list):
    mess = f'Вы ввели: {list_numbers}'
    i = len(list_numbers)
    median = None
    while i > 1:
        max_num = max(list_numbers)
        list_numbers.remove(max_num)
        min_num = min(list_numbers)
        list_numbers.remove(min_num)
        i -= 2
        median = list_numbers[0]
    return f'{mess}\nМедиана: {median}\n'

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
0.002544400000000002
Время исполнения для массива длиной 100 элементов:
0.0656727
Время исполнения для массива длиной 1000 элементов:
4.452351
"""
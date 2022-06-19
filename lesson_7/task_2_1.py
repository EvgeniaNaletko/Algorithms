"""
Задание 2. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные по длине части:
в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
Решите задачу тремя способами:
1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла, Кучей)
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit

# Гнмья сортировка. Она идёт от начала массива до конца и сравнивает соседние элементы.
# Если два соседних элемента пришлось поменять местами, то сортировка возвращается на шаг назад

def gen_list(m=10):
    my_list = [randint(-100, 100) for i in range(m * 2 + 1)]
    return my_list

def get_median(list_numbers):
    mess = f'Вы ввели: {list_numbers}'
    i = 1
    while i < len(list_numbers):
        if list_numbers[i - 1] <= list_numbers[i]:
            i += 1
        else:
            list_numbers[i - 1], list_numbers[i] = list_numbers[i], list_numbers[i - 1]
            if i > 1:
                i -= 1
    median = list_numbers[len(list_numbers) // 2]

    return f'{mess}\nОтсортированный: {list_numbers}\nМедиана: {median}\n'

#print(get_median(gen_list()))
#print(get_median(gen_list(5)))


print('Время исполнения для массива длиной 10 элементов:')
print(timeit("get_median(gen_list()[:])", globals=globals(), number=100))
print('Время исполнения для массива длиной 100 элементов:')
print(timeit("get_median(gen_list(100)[:])", globals=globals(), number=100))
print('Время исполнения для массива длиной 1000 элементов:')
print(timeit("get_median(gen_list(1000)[:])", globals=globals(), number=100))


"""
Время исполнения для массива длиной 10 элементов:
0.005314400000000004
Время исполнения для массива длиной 100 элементов:
0.3780046
Время исполнения для массива длиной 1000 элементов:
31.8887738
"""
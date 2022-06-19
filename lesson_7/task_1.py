"""
Задание 1.
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее)!
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли доработка и в каких случаях
она будет эффективной.
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере, а по убыванию.
"""
from random import randint
from timeit import timeit

def gen_list():
    my_list = [randint(-100, 100) for i in range(100)]
    return my_list

sort_list = [50, 49, 48, 45, 44, 30, 29, 25, 23, 22, 9, 8, 6, 4, 3, 2, -6, -25, -75, -100]

# Без доработки

def bubble_sort(list_numbers):
    mess = f'Вы ввели: {list_numbers}'
    for i in range(len(list_numbers)):
        for j in range(len(list_numbers) - 1):
            if list_numbers[j] < list_numbers[j + 1]:
                list_numbers[j], list_numbers[j + 1] = list_numbers[j + 1], list_numbers[j]
    return f'{mess}\nОтсортированный: {list_numbers}\n'

#print(bubble_sort(gen_list()))
#print(bubble_sort(sort_list))


# С доработкой
def bubble_sort_2(list_numbers):
    mess = f'Вы ввели: {list_numbers}'
    list_copy = list_numbers.copy()
    for i in range(len(list_copy)):
        for j in range(len(list_copy) - 1):
            if list_copy[j] < list_copy[j + 1]:
                list_copy[j], list_copy[j + 1] = list_copy[j + 1], list_copy[j]
        if list_copy == list_numbers:
            return f'{mess}\nОн уже отсортирован! Список: {list_copy}\n'
    return f'{mess}\nОтсортированный: {list_copy}\n'

#print(bubble_sort_2(gen_list()))
#print(bubble_sort_2(sort_list))


print('Время исполнения первой функции:')
print(timeit("bubble_sort(gen_list()[:])", globals=globals(), number=10000))
print('Время исполнения второй функции:')
print(timeit("bubble_sort_2(gen_list()[:])", globals=globals(), number=10000))
print('Время исполнения первой функции. Отсортированный список: ')
print(timeit("bubble_sort(sort_list[:])", globals=globals(), number=50000))
print('Время исполнения второй функции. Отсортированный список: ')
print(timeit("bubble_sort_2(sort_list[:])", globals=globals(), number=50000))

"""
Время исполнения первой функции:
8.7220387
Время исполнения второй функции:
8.534314100000001
Время исполнения первой функции. Отсортированный список: 
1.3893315000000008
Время исполнения второй функции. Отсортированный список: 
0.25304669999999874

Вывод: вторая функция сортирует список быстрее. Также ее преимущество в том, что она распознает уже отсортированный
список и не делает лишних действий
"""
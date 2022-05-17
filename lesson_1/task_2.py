"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""

from random import sample

# Первый способ. Сложность: O(n).
def get_min_number_1(lst_obj):

    min_number = lst_obj[0]     # O(1)
    for i in lst_obj:           # O(n)
        if i < min_number:      # O(1)
            min_number = i      # O(1)
    return min_number           # O(1)


# Второй способ. Сложность: O(n**2).
def get_min_number_2(lst_obj):

    min_number = lst_obj[0]                                       #О(1)
    for i in lst_obj:                                             #О(n)
        for j in range(lst_obj.index(i) + 1, len(lst_obj) - 1):   #О(n)
            if min_number > lst_obj[j]:                           #О(1)
                min_number = lst_obj[j]                           #О(1)
    return min_number                                             #О(1)



for j in (5, 10, 15):
    lst = sample(range(-1000, 1000), j)

print(lst, 'минимальное', get_min_number_1(lst))
print(lst, 'минимальное', get_min_number_2(lst))
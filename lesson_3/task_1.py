'''Реализуйте функции:
a) заполнение списка, оцените сложность в O-нотации
   заполнение словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
b) получение элемента списка, оцените сложность в O-нотации
   получение элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
с) удаление элемента списка, оцените сложность в O-нотации
   удаление элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!'''

from time import time

def time_function(func):
    def wrapper(*args):
        start = time()
        res = func(*args)
        end = time()
        print(f'Время выполнения: {end - start} сек')
        return res
    return wrapper

n = 10 ** 7

# 1: заполнение

@time_function
def list_append(some_list):
    """Заполнение списка. Сложность О(n)"""
    for i in range(n):
        some_list.append(i)

new_list = []
print('Заполнение списка. ', end='')
list_append(new_list)

@time_function
def dict_append(some_dict):
    """Заполнение словаря. Сложность О(n)"""
    for i in range(n):
        some_dict[i] = i

new_dict = {}
print('Заполнение словаря. ', end='')
dict_append(new_dict)
print()

# 2: получение элемента

@time_function
def check_list(some_list):
    """Получение элементов списка. Сложность O(n)"""
    for i in range(n):
        a = some_list[i]
    return a

print('Получение элемента списка. ', end='')
check_list(new_list)

@time_function
def check_dict(some_dict):
    """"Получение элементов словаря. Сложность O(n)"""
    for i in range(n):
        a = some_dict[i]
    return a

print('Получение элемента словаря. ', end='')
check_dict(new_dict)
print()

# 3: Удаление элемента

@time_function
def del_list(some_list):
    """Удаление элемента списка. Сложность O(n ** 2)"""
    for i in range(len(some_list)):
        del some_list[-1]
    return some_list

print('Удаление элемента списка. ', end='')
del_list(new_list)

@time_function
def del_dict(new_dict):
    """Удаление элемента словаря. Сложность O(n)"""
    for i in range(n):
        new_dict.pop(i)
    return new_dict

print('Удаление элемента словаря. ', end='')
del_dict(new_dict)

''''Так как большенство операций по словарю имеют константную сложность, они быстрее чем у списков'''
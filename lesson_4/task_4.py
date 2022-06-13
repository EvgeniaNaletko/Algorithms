"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from timeit import default_timer
from collections import OrderedDict
from random import randint

new_dict = {}
new_ordereddict = OrderedDict()
n = 10 ** 6

def time_decor(func):
    def wrapper(*args, **kwargs):
        start = default_timer()
        result = func(*args, **kwargs)
        print(f'Время выполнения: {default_timer() - start}')
        print('-' * 50)
        return result
    return wrapper()

@time_decor
def fill_dict():
    """
    Заполнение словаря
    """
    for i in range(n):
        new_dict[i] = randint(- n, n)
    print('Словарь заполнен')

@time_decor
def fill_ordereddict():
    """
    Заполнение OrderedDict
    """
    for i in range(n):
        new_ordereddict[i] = randint(- n, n)
    print('OrderedDict заполнен')

@time_decor
def edit_dict():
    for key in new_dict.keys():
        new_dict[key] = randint(- n, n)
    print('Словарь изменен')

@time_decor
def edit_ordereddict():
    for key in new_ordereddict.keys():
        new_ordereddict[key] = randint(- n, n)
    print('Ordereddict изменен')

@time_decor
def del_dict():
    for i in range(n):
        new_dict.pop(i)
    print('Словарь удален')

@time_decor
def del_ordereddict():
    for i in range(n):
        new_ordereddict.pop(i)
    print('OrderedDict удален')

'''
Словарь заполнен
Время выполнения: 0.1014234
--------------------------------------------------
OrderedDict заполнен
Время выполнения: 0.1807033
--------------------------------------------------

Вывод: OrderedDict заполняется медленнее обычного словаря


Словарь изменен
Время выполнения: 0.12353459999999994
--------------------------------------------------
Ordereddict изменен
Время выполнения: 0.1979746
--------------------------------------------------

Вывод: изменение значений также быстрее у обычного словаря


Словарь удален
Время выполнения: 0.24964700000000006
--------------------------------------------------
OrderedDict удален
Время выполнения: 0.3198175
--------------------------------------------------

Вывод: удаление быстрее у обычного словаря

OrderedDict уступает обычному словарю в скорости, но его можно использовать если нужны специфичные методы
'''
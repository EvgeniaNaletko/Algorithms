"""
Задача 3.
В соответствии с документацией Python, deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
1) сравнить операции append, pop, extend списка и дека и сделать выводы что и где быстрее
2) сравнить операции appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
3) сравнить операции получения элемента списка и дека и сделать выводы что и где быстрее
Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
from collections import deque
from timeit import timeit
from random import randint

n = 10 ** 5
new_list = [i for i in range(n)]
new_deque = deque([i for i in range(n)])

# 1

def append_list(new_list):
    for i in range(n):
        new_list.append(i)
    return new_list

def append_deque(new_deque):
    for i in range(n):
        new_deque.append(i)
    return new_deque

print('-' * 20, 'append, pop, extend', '-' * 20)
print(timeit('append_list(new_list)', globals=globals(), number=100))
print(timeit('append_deque(new_deque)', globals=globals(), number=100))
print()

def pop_list(new_list):
    for i in range(n):
        new_list.pop()

def pop_deque(new_deque):
    for i in range(n):
        new_deque.pop()

print(timeit('pop_list(new_list)', globals=globals(), number=100))
print(timeit('pop_deque(new_deque)', globals=globals(), number=100))
print()

def extend_list(new_list):
    new_list.extend(randint(- n, n))

def extend_deque(new_deque):
    new_deque.extend(randint(- n, n))

print(timeit('extend_list(new_list)', globals=globals(), number=100))
print(timeit('extend_deque(new_deque)', globals=globals(), number=100))
print()

# 2

def appendleft_list(new_list):
    for i in range(n):
        new_list.insert(0, i)

def appendleft_deque(new_deque):
    for i in range(n):
        new_deque.appendleft(i)

print('-' * 20, 'appendleft, popleft, extendleft', '-' * 20)
print(timeit('appendleft_list(new_list)', globals=globals(), number=100))
print(timeit('appendleft_deque(new_deque)', globals=globals(), number=100))
print()

def popleft_list(new_list):
    for i in range(len(new_list)):
        new_list.pop(0)

def popleft_deque(new_deque):
    for i in range(n):
        new_deque.popleft()

print(timeit('popleft_list(new_list)', globals=globals(), number=100))
print(timeit('popleft_deque(new_deque)', globals=globals(), number=100))
print()

def extendleft_list(new_list):
    for i in range(n):
        new_list.insert(0, randint(- n, n))

def extendleft_deque(new_deque):
    for i in range(n):
        new_deque.extendleft(randint(- n, n))

print(timeit('extendleft_list(new_list)', globals=globals(), number=100))
print(timeit('extendleft_deque(new_deque)', globals=globals(), number=100))
print()

# 3

def chek_list(new_list):
    for i in range(n):
        elem = new_list[randint(0, len(new_list) - 1)]

def chek_deque(new_deque):
    for i in range(n):
        elem = new_deque[randint(0, len(new_deque) - 1)]

print('-' * 20, 'получение рандомного элемента', '-' * 20)
print(timeit('chek_list(new_list)', globals=globals(), number=100))
print(timeit('chek_deque(new_deque)', globals=globals(), number=100))


'''
-------------------- append, pop, extend --------------------
1.6239598
1.5525064000000002

0.9602946000000006
0.8592305999999999

1.54264361900000002
1.54306029100000005
Вывод: методы append, pop и extend выполняются примерно за одно время и у list, и у deque

-------------------- appendleft, popleft, extendleft --------------------
65.923262900000001
0.1175921000000001015

35.1620649000000002
0.215184899999999715

66.8101304000000003
0.45788100000000007
Вывод: методы appendleft, popleft и extendleft выполняются у deque гораздо быстрее

-------------------- получение рандомного элемента --------------------
0.09186840000000096
1.2039445999999998
Вывод: поиск элемента быстрее у list
'''
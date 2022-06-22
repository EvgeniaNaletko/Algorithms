"""
Задание 1.
Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
2) тема понятна? постарайтесь сделать свою реализацию. Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""
from collections import Counter, deque

class Node:

    __slots__ = ['left', 'right']

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def __repr__(self):
        return f'0{self.left},1{self.right}'

class Haffman:

    __slots__ = ['result', 'code_table', 'nod_dict']

    def __init__(self):
        self.nod_dict = []
        self.code_table = {}
        self.result = ''

    def count(self, s):
        return deque(sorted(Counter(s).items(), key=lambda x: x[1]))

    def tree(self, new_deque):

        while len(new_deque) > 1:

            weight = new_deque[0][1] + new_deque[1][1]
            node = Node(left=new_deque.popleft()[0], right=new_deque.popleft()[0])

            for i, el in enumerate(new_deque):
                if weight <= el[1]:
                    new_deque.insert(i, (node, weight))
                    break
            else:
                new_deque.append((node, weight))

        return new_deque[0][0]

    def haffman_code_table(self, node, path=''):

        if not isinstance(node, Node):
            self.code_table.setdefault(node, path)
        else:
            self.haffman_code_table(node.left, f'{path}0')
            self.haffman_code_table(node.right, f'{path}1')

    def code(self, s):
        self.nod_dict = self.tree(self.count(s))
        self.haffman_code_table(self.nod_dict)

        for c in s:
            self.result = f'{self.result} {self.code_table[c]}'

        return self.result


#s = input("Введите строку для кодирования: ")

s = "beep boop beer!"
haffman = Haffman()

print(haffman.code(s))
print(haffman.code_table)

"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте класс-структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class TaskBoard:
    def __init__(self):
        self.queue = QueueClass()
        self.register = []

    def resolve_task(self):
        task = self.queue.from_queue()
        self.register.append(task)

    def to_current_queue(self, item):
        self.queue.to_queue(item)

    def current_task(self):
        return self.queue.elems[len(self.queue.elems) - 1]



task_board = TaskBoard()
task_board.to_current_queue(1)
task_board.to_current_queue(2)
task_board.to_current_queue(3)
task_board.to_current_queue(4)
print(task_board.queue.elems)
print(task_board.current_task())
task_board.resolve_task()
print(task_board.queue.elems)


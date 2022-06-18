"""
Задание 1.
Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ курсов Алгоритмы и Основы Python
На каждый скрипт нужно два решения - исходное и оптимизированное.
Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler
Вам нужно написать аналитику, что вы сделали для оптимизации памяти и чего добились.
ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те, где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это отговорки.
Примеров оптимизации мы перечислили много: переход с массивов на генераторы, numpy,
использование слотов, применение del, сериализация и т.д.
Это файл для четвертого скрипта
"""
from pympler import asizeof

'''
Курс основ. Дз 9, задание 3. Применили слоты и сэкономили память 
'''

# До
class Worker:

    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


    def get_full_name(self) -> str:
        """Возвращает строку по формату 'Имя Фамилия'"""
        return f'{self.name} {self.surname}'.title()


    def get_total_income(self) -> int:
        """Возвращает суммарный ежемесячных доход"""
        return sum(value for value in self._income.values())


welder = Worker('иван', 'васильев', 'сварщик', {'wage': 50000, 'bonus': 15000})
driver = Worker('петр', 'николаев', 'водитель', {'wage': 30000, 'bonus': 7500})
scientist = Worker('геннадий', 'разумов', 'ученый', {'wage': 150000, 'bonus': 25000})
print(welder.get_full_name(), welder.get_total_income())  # Иван Васильев 65000
print(driver.get_full_name(), driver.get_total_income())  # Петр Николаев 37500
print(scientist.get_full_name(), scientist.get_total_income())  # Геннадий Разумов 175000
print(asizeof.asizeof(scientist))

# После
class Worker_2:
    __slots__ = ('name', 'surname', 'position', '_income',)

    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


    def get_full_name(self) -> str:
        """Возвращает строку по формату 'Имя Фамилия'"""
        return f'{self.name} {self.surname}'.title()


    def get_total_income(self) -> int:
        """Возвращает суммарный ежемесячных доход"""
        return sum(value for value in self._income.values())


welder_2 = Worker_2('иван', 'васильев', 'сварщик', {'wage': 50000, 'bonus': 15000})
driver_2 = Worker_2('петр', 'николаев', 'водитель', {'wage': 30000, 'bonus': 7500})
scientist_2 = Worker_2('геннадий', 'разумов', 'ученый', {'wage': 150000, 'bonus': 25000})
print(welder_2.get_full_name(), welder_2.get_total_income())  # Иван Васильев 65000
print(driver_2.get_full_name(), driver_2.get_total_income())  # Петр Николаев 37500
print(scientist_2.get_full_name(), scientist_2.get_total_income())  # Геннадий Разумов 175000
print(asizeof.asizeof(scientist_2))



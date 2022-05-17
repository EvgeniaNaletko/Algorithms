"""
Задание 3.
Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

# Первый способ. Сложность: O(n log n).
def search_profit_company(company):

    profit_company = []                                             #O(1)
    value = []                                                      #O(1)
    for val in company.values():                                    #O(n)
        value.append(val)                                           #O(1)
        value.sort(reverse=True)                                    #O(n log n)

    i = 0                                                           #O(1)
    while i < 3:                                                    #O(1)
        for key, val in company.items():                            #O(n)
            if val == value[i]:                                     #O(1)
                profit_company.append(f'{key} с заработком {val}')  #O(1)
        i += 1                                                      #O(1)

    return f'Компании с наибольшим заработком: {profit_company}'    #O(1)


# Второй способ. Сложность: O(n**2).
def search_profit_company_2(company):

    max_profit_2 = []                                                     #O(1)
    max_value_key = 0                                                     #O(1)
    while len(max_profit_2) < 3:                                          #O(n)
        max_value = 0                                                     #O(1)
        for key, value in company.items():                                #O(n)
            if max_value < value:                                         #O(1)
                max_value = value                                         #O(1)
                max_value_key = key                                       #O(1)
        max_value = company.pop(max_value_key)                            #O(1)
        max_profit_2.append(f'{max_value_key} с заработком {max_value}')  #O(1)
    return f'Компании с наибольшим заработком: {max_profit_2}'            #O(1)


"""
Первая реализация будет эффективнее
"""

company = {'name _0': 400,'name_1': 90000,'name_2': 89999, 'name_3': 10000,
           'name_4':87777,'name_5': 10,'name_6': 99999, 'name_7': 800}

print(search_profit_company(company))
print(search_profit_company_2(company))
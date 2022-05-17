"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

#Первый способ. Сложность: O(n)
def authorization_1(users, name, password):
    for key, value in users.items():                                              #O(n)
        if key == name:                                                           #O(1)

            if value['password'] != password:                                     #O(1)
                return "Пароль не верный"                                         #O(1)

            elif value['password'] == password and value['activation'] == False:  #O(1)
                return "Пройдите активацию"                                       #O(1)

            elif value['password'] == password and value['activation'] == True:   #O(1)
                return "Добро пожаловать"                                         #O(1)

    return "Пользователя не существует"                                           #O(1)


# Второй способ Сложность: O(1)
def authorization_2(users, name, password):
    if users.get(name):                                                                    #O(1)

        if users[name]['password'] != password:                                            #O(1)
            return "Пароль не верный"                                                      #O(1)

        elif users[name]['password'] == password and users[name]['activation'] == False:   #O(1)
            return "Пройдите активацию"                                                    #O(1)

        elif users[name]['password'] == password and users[name]['activation'] == True:    #O(1)
            return "Добро пожаловать"                                                      #O(1)

    return "Пользователя не существует"                                                    #O(1)

"""
Вторая реализация будет эффективнее, так как в ней не используется цикл
"""


users = {'name_1': {'password': '123', 'activation': True},
         'name_2': {'password': '1234', 'activation': False},
         'name_3': {'password': '12345', 'activation': True}}

print(authorization_1(users, 'name_1', '123'))
print(authorization_1(users, 'name_2', '1234'))
print(authorization_1(users, 'name_3', '12'))
print(authorization_1(users, 'name_10', '123'))

print(authorization_2(users, 'name_1', '123'))
print(authorization_2(users, 'name_2', '1234'))
print(authorization_2(users, 'name_3', '12'))
print(authorization_2(users, 'name_10', '123'))
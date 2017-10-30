"""
Написати функцію, яка буде приймати декілька значень,
одне з яких значення за замовченням(повинна бути перевірка
на наявність), і у випадку якщо воно є додати його до
іншого агрументу, якщо немає - придумайте логіку що робити программі.
"""


a = 2

# function calculates sum of <a> and other arguments
# input data: a - type number, default value None, *args - type number, optional arguments
# return number type: sum of <a> and all *args; if a not specified function return 0
def sum (a = None, *args):
        if a is None:
            a = 0
        else:
            for i in args:
                a = a + i
        return a
print(sum())
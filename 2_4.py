"""
Створіть 2 змінні x та y з довільними значеннями;
Створіть просту умовну конструкцію(звісно вона повинна бути в тілі ф-ції), під час виконання якої буде перевірятися рівність змінних x та y.
Удоскональте конструкцію та додайте відповідні умови, які б при нерівності змінних х та у відповідь повертали різницю чисел.
Повинні опрацювати такі умови:
x > y; відповідь - х більше ніж у на z
x < y; відповідь - у більше ніж х на z
x==y. відповідь - х дорівнює z
"""
import random
#two random variable number typy in range 0-10
x = random.randint(0,10)
y = random.randint(0,10)

# function will compare two random variables
# input data: x,y - number type
# return number type: in the case of inequality division greater number and less number;
#                     in case equality on of the number x or y
def equation(x,y):
    if x > y:
        return x-y
    elif y > x:
        return y-x
    else:
        return x

print (equation(x,y))
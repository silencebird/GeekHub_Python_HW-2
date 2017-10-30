"""
Створіть 3 різних функції(на ваш вибір), кожна з
цих функцій повинна повертати якийсь результат.
Також створіть четверу ф-цію, яка в тілі викликає
3 попередні, обробляє повернутий ними результат та
також повертає результат. Таким чином ми будемо
викликати 1 функцію, а вона в своєму тілі ще 3
"""
import math

# the result will be the area of the triangle with sides  a,b,c

# function check can we create triangle with sides a,b,c
# input data: a,b,c - type number, sides of triangle
# return  boolean type: true, if we can create triangle, and false - if it is impossible with this sides(a,b,c)
def is_triangle(a,b,c):
    return (a + b > c) and (b + c > a) and (a + c > b)

# function calculates a perimeter of triangle with sides a,b,c
# input data: a,b,c - type number, sides of triangle
# return number type: half perimeter of the triangle with sides a,b,c
def half_perimeter(a,b,c):
    return (a+b+c)/2

# fubction will find altitude on side a in triangle with sides a,b,c
# input data: a,b,c - type number, sides of triangle; p - half perimeter of triangle with sides a,b,c
# return number type: altitude length
def altitude(a,b,c,p):
     return math.sqrt(2*(p*(p-a)*(p-b)*(p-c)))/a

# function will find area of the triangle with sides a,b,c
# input data: a,b,c - type number, sides of triangle
# return number type: area of triangle with sides a,b,c
def triangel_area(a,b,c):
    if is_triangle(a,b,c):
        p = half_perimeter(a,b,c)
        return a*altitude(a,b,c,p)/2

print(triangel_area(3,4,5))
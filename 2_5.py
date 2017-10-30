"""
маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клаві
створюєте ф-цію яка буде отримувати рядки на зразок мого, яка працює в 4 випадках:
якщо довжина рядка в дфапазоні 30-50 -> прінтує довжину, кількість букв та цифр
якщо довжина менше 30 -> прінтує суму всіх чисел та окремо рядок без цифр лише з буквами
якщо довжина бульше 50 - > ваша фантазія
звысно 4 все інше
"""
import math


s = "asfdasfs7432435435435fggtrgrtg4565fsf9dfds"

# function will separeted numbers and alphabetic letters in  number_string and alphabet_string
# input data: s - string
# return two strings: number_string, alphabet_string
def separator(s):
    number_string = ""
    alphabet_string = ""
    for ch in s:
        if ch.isdigit():
            number_string += ch
        if ch.isalpha():
            alphabet_string += (ch)
    return number_string, alphabet_string

"""
function will separeted numbers and alphabetic leters in  number_string and alphabet_string
input data: s - string
return if length of input string: less 30 - sum of numbers in the string and string contains only alphabetic letters form the string s
                                  from 30 to 50 - length of string s, two strings: first - all numbers from string s, second - all alphsbetic letters from string s
                                  under 50 - max and min number in string s
                                  other cases - if variable not string type
"""
def str (s):
    if len(s) < 30:
        j = 0
        for i in separator(s)[0]:
            j += int(i)
        return ("sum of the numbers from string: ", j, "string only alphabetic letters: ",separator(s)[1])
    if (len(s) >= 30) and (len(s) <= 50):
        return("number sum: ", len(s), "string only numbers: ", separator(s)[0], "string only alphabetic letters: ", separator(s)[1])
    if len(s) > 50 :
        numbers = tuple(separator(s)[0])
        return max(numbers), min(numbers)
    if not isinstance(s,str):
        return(" this function work only with string type.")

print(str(s))
"""
(таких ф-цій потрібно написати 3 -> різними варіантами) Написати функцію
season, приймаючу 1 аргумент — номер місяця (від 1 до 12), яка буде
повертати пору року, якій цей місяць належить (зима, весна, літо або осінь).
"""

x = 0

# the function will find the month by its number
# input data: x - number of month
# return  strings: name of season
# if number of month in year not exist will output string "month not exist"
def season(x):
    if (x == 12) or (x == 1) or (x == 2):
        return "winter"
    elif (x >= 3) and (x <= 5):
        return "spring"
    elif (x >= 6) and (x <= 8):
        return "summer"
    elif (x >= 9) and (x <= 11):
        return "autumn"
    else :
        return "month not exist"

print(season(x))
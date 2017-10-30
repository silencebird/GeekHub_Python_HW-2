"""
(таких ф-цій потрібно написати 3 -> різними варіантами) Написати функцію
season, приймаючу 1 аргумент — номер місяця (від 1 до 12), яка буде
повертати пору року, якій цей місяць належить (зима, весна, літо або осінь).
"""
season_list = {
    "winter" : {
        12: "December",
        1: "January",
        2: "February"
    },
    "spring" : {
        3:  "March",
        4:  "April",
        5:  "May"
    },
    "summer" : {
        6:  "June",
        7:  "Jule",
        8:  "August"
    },
    "autumn": {
        9:  "September",
        10:  "October",
        11:  "November"
    }
}

# x - month number
x = 11

# the function will find the month by its number
# input data: x - number of month
# return  strings: name of season
# if number of month in year not exist will output string "This month not exist"

def season(x):
    for i in season_list:
        if x in season_list[i].keys():
            return i
    return "This month not exist"

print(season(x))

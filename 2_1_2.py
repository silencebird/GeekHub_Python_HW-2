"""
(таких ф-цій потрібно написати 3 -> різними варіантами) Написати функцію
season, приймаючу 1 аргумент — номер місяця (від 1 до 12), яка буде
повертати пору року, якій цей місяць належить (зима, весна, літо або осінь).
"""


season = {
    1: "winter",
    2: "winter",
    3: "spring",
    4: "spring",
    5: "spring",
    6: "summer",
    7: "summer",
    8: "summer",
    9: "autumn",
    10:"autumn",
    11:"autumn",
    12:"winter"
}
x = 2

print(season.get(x,"month not exist"))


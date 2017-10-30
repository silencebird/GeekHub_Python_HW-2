"""
ну і традиційно -> калькулятор повинна бути 1 ф-ція яка б приймала 3 аргументи - один з яких операція яку зробити!
"""
calc_operation = {"+", "-", "*", "/", "^"}

# function will find result of an arithmetic operation between a and b
# input data: a,b - number type, operation - string type, allowed values:
#                      "+" - addition, "-" - subtraction, "*" - multiplication, "/" - division, "^" - a in power b
# return number type: result of calculation
# if operation not allowed well return string "This calculator don't have this operation"
def calc(a, b, operation):
    if operation == "+":
        return a + b
    if operation == "-":
        return a - b
    if operation == "*":
        return a * b
    if operation == "/":
        return a / b
    if operation == "^":
        return a ** b
    if not (operation in calc_operation):
        return "This calculator don't have this operation"

print (calc(2,2,"^"))

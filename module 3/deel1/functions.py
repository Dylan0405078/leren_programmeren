import os
def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    if number2 == 0:
        return "Error: Division by zero is not allowed."
    else:
        return number1 / number2

def increment(number1):
    return number1 + 1

def decrement(number1):
    return number1 - 1

def double(number1):
    return number1 * 2

def halve(number1):
    return number1 / 2

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
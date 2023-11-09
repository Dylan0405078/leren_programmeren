# example:
def increment(nr: float) -> float:
  return nr + 1

def decrement(nr: float) -> float:
  return nr - 1

def add(num1: float, num2: float) -> float:
  return num1 + num2

def subtract(num1: float, num2: float) -> float:
  return num1 - num2

def multiply(num1: float, num2: float) -> float:
  return num1 * num2

def divide(num1: float, num2: float) -> float:
  try:
    if num2 == 0:
        return None
    result = num1 / num2
    return result
  except ZeroDivisionError:
    return "Error: Division by zero is not allowed."




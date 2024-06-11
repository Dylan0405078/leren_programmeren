def times2(base:int) -> int:
    return times(base, 2)

def times3(base:int) -> int:
    return times(base, 2)

def times(base:int, multiplier:int) -> int:
    return base * multiplier

value1 = times2(5)
value2 = times3(5)


print(value1 + value2)
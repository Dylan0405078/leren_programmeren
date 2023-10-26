#vergelijk getallen

def vergelijk_getallen(nr1: int, nr2: int) -> str:
    if nr1 == nr2:
        return 'Beide getallen zijn even groot'
    elif nr1 > nr2:
        return f'Maximum: {nr1} en minimum: {nr2}'
    else:
        return f'Maximum: {nr2} en minimum: {nr1}'

a = int(input("Voer het eerste gehele getal in: "))
b = int(input("Voer het tweede gehele getal in: "))

resultaat = vergelijk_getallen(a, b)
print(resultaat)

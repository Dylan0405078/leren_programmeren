import functions

firstRound = True

print("Wat wilt u doen?")
choice = input("A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren? ")

if choice in ['A', 'B', 'C', 'D']:
    n1 = float(input("Voer het eerste getal in: "))
    n2 = float(input("Voer het tweede getal in: "))
elif choice in ['E', 'F']:
    n1 = float(input("Voer het getal in: "))
    n2 = 1
elif choice in ['G', 'H']:
    n1 = float(input("Voer het getal in: "))
    n2 = 2
else:
    print("Ongeldige keuze.")
    firstRound = False

while not firstRound:
    print(f"Wil je wat met de uitkomst ({n1}) doen?")

    choice = input("A) iets optellen, B) iets aftrekken, C) met iets vermenigvuldigen, D) ergens door delen, E) ophogen, F) verlagen, G) verdubbelen, H) halveren of I) niets? ")

    if choice == 'I':
        print("Programma gestopt.")
        break

    if choice not in ['A', 'B', 'C', 'D']:
        print("Ongeldige keuze.")
        continue

    if choice in ['A', 'B', 'C', 'D']:
        n2 = float(input("Voer het tweede getal in: "))
    elif choice == 'E':
        n2 = 1
    elif choice == 'F':
        n2 = -1
    elif choice == 'G':
        n2 = 2
    elif choice == 'H':
        n2 = 0.5

    if choice == 'A':
        result = functions.addition(n1, n2)
        print(f"{n1} + {n2} = {result}")
    elif choice == 'B':
        result = functions.subtraction(n1, n2)
        print(f"{n1} - {n2} = {result}")
    elif choice == 'C':
        result = functions.multiplication(n1, n2)
        print(f"{n1} * {n2} = {result}")
    elif choice == 'D':
        if n2 == 0:
            print("Kan niet delen door 0!")
            continue
        result = functions.division(n1, n2)
        print(f"{n1} : {n2} = {result}")
    elif choice == 'E':
        result = functions.addition(n1, n2)
        print(f"{n1} + {n2} = {result}")
    elif choice == 'F':
        result = functions.subtraction(n1, n2)
        print(f"{n1} - {n2} = {result}")
    elif choice == 'G':
        result = functions.multiplication(n1, n2)
        print(f"{n1} * {n2} = {result}")
    elif choice == 'H':
        result = functions.multiplication(n1, n2)
        print(f"{n1} * {n2} = {result}")

    firstRound = False
    n1 = result

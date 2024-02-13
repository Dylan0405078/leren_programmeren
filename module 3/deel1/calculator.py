# rekenmachine.py
import functions

def main():
    firstRound = True
    n1 = False

    while True:
        if firstRound:
            print("Wat wilt u doen?")
        else:
            print("Wil je wat met de uitkomst doen?")
            
        if firstRound:
            choice = input("A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren? ")
        else:
            choice = input("A) iets optellen, B) iets aftrekken, C) met iets vermenigvuldigen, D) ergens door delen, E) ophogen, F) verlagen, G) verdubbelen, H) halveren of I) niets? ")

        if choice == 'I':
            print("Programma gestopt.")
            break

        if firstRound:
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
                continue
        else:
            if choice in ['A', 'B', 'C', 'D']:
                n2 = float(input("Voer het tweede getal in: "))
            else:
                print("Ongeldige keuze.")
                continue

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
            result = functions.division(n1, n2)
            print(f"{n1} : {n2} = {result}")
        elif choice == 'E':
            result = functions.addition(n1, n2)
            print(f"{n1} + 1 = {result}")
        elif choice == 'F':
            result = functions.subtraction(n1, n2)
            print(f"{n1} - 1 = {result}")
        elif choice == 'G':
            result = functions.multiplication(n1, n2)
            print(f"{n1} * 2 = {result}")
        elif choice == 'H':
            result = functions.division(n1, n2)
            print(f"{n1} : 2 = {result}")

        firstRound = False
        n1 = result

if __name__ == "__main__":
    main()

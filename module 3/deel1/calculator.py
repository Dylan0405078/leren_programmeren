import functions
import time

firstRound = True
n1 = 0  

while True:
    if firstRound:
        print("Wat wilt u doen?")
    else:
        print(f"Wil je wat met de uitkomst ({n1}) doen?")
    
    options = "A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren? " if firstRound else "A) iets optellen, B) iets aftrekken, C) met iets vermenigvuldigen, D) ergens door delen, E) ophogen, F) verlagen, G) verdubbelen, H) halveren of I) niets? "
    choice = input(options).upper()

    if choice == 'I':
        print(f'het eindresultaat is: {n1}')
        print("Programma sluit zich af.....")
        time.sleep(3)
        functions.clear_console()
        break

    if firstRound:
        n1 = functions.ask_for_number('voer het eerste getal in:')
        n2 = functions.ask_for_number('voer het tweede getal in:')

        
    else:
        if choice in ['A', 'B', 'C', 'D']:
            n2 = functions.ask_for_number('voer het tweede getal in:')
        elif choice in ['E', 'F', 'G', 'H']:
            n2 = 1 if choice in ['E', 'F'] else 2
        else:
            print("Ongeldige keuze.")
            continue

    if choice == 'D' and n2 == 0:
        print("Kan niet delen door 0!")
        continue

    result = getattr(functions, {'A': 'addition', 'B': 'subtraction', 'C': 'multiplication', 'D': 'division', 'E': 'addition', 'F': 'subtraction', 'G': 'multiplication', 'H': 'division'}[choice])(n1, n2)

    print(f"Uitkomst: {result}")
    firstRound = False
    n1 = result

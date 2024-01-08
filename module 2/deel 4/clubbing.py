# leeftijd vraag eruit halen 
#vip lijst gebruiken
# vip vervolg aanpassen
#functies niet onnodig gebruiken


# Functie voor het controleren van leeftijd
def check_valid_age(age):
    while age < 0 or age > 150:
        age = int(input("Ongeldige leeftijd. Voer alstublieft een geldige leeftijd in: "))
    return age


# Variabelen
name = input('Wat is je naam? ')
age = int(input("Wat is je leeftijd? "))
age = check_valid_age(age)


# Constanten
VIP_LIJST = ['Jouke', 'Jeroen', 'Rudi']
BANDJE_ROOD = False
BANDJE_BLAUW = False
VIP = name.lower() in [x.lower() for x in VIP_LIJST]
STEMPEL = age > 20
PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30


# Functionaliteit clubbing
if age < 18:
    difference = 18 - age
    print(f"Sorry, je bent niet oud genoeg. Probeer het over {difference} jaar.")
else:
    drinken = input('Wat wil je drinken? ')
    if drinken == "champagne":
        if not BANDJE_ROOD and not BANDJE_BLAUW and not VIP:
            print("Sorry, champagne is alleen voor VIP.")
        elif BANDJE_ROOD:
            print("Je hebt een rood bandje en kunt geen champagne bestellen.")
        else:
            print(f"Aub, hier is je champagne dat wordt dan {PRIJS_CHAMPAGNE},-")
    elif drinken == "cola":
        if VIP:
            print(f"Aub, hier heb je cola, mijn complimenten vanuit het huis!")
        else:
            print(f"Aub, je cola dat wordt dan {PRIJS_COLA},-")
    elif drinken == "bier":
        if BANDJE_BLAUW or STEMPEL or VIP:
            print(f'Aub, hier heb je een lekkere pils, dat wordt dan {PRIJS_BIER}!')
        elif BANDJE_ROOD or not VIP:
            print('Je hebt een rood bandje en kunt geen bier bestellen.')
    else:
        print('Ik weet niet wat je bedoelt, hier heb je een glas water.')

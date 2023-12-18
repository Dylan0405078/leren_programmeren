PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST =['jeroen', 'jouke', 'rudi'] 



def calculate_age_difference(age):
    return 18 - age

def ask_question(question):
    response = input(question + " ")
    return response

def check_valid_age(age):
    while age < 0 or age > 150:
        age = int(input("Ongeldige leeftijd. Voer alstublieft een geldige leeftijd in: "))
    return age

def main():
    age = ask_question("Hoe oud ben je?")
    age = check_valid_age(int(age))

    if age < 18:
        difference = calculate_age_difference(age)
        print(f"Sorry, je bent niet oud genoeg. Probeer het over {difference} jaar.")
    else:
        name = ask_question("Wat is je naam?")
        vip = ask_question("Wil je VIP zijn? (ja/nee)")

        if vip.lower() == "ja" and name.lower() in VIP_LIST:
            over_21 = ask_question("Ben je ouder dan 21? (ja/nee)")

            if over_21.lower() == "ja":
                kleur = "blauw"
                print(f"Je krijgt van mij een Blauw {kleur} bandje.")
            else:
                kleur = "rood"
                print(f"Je krijgt van mij een Rood {kleur} bandje.")
        else:
            over_21 = ask_question("Ben je ouder dan 21? (ja/nee)")

            if over_21.lower() == "ja":
                print("Je krijgt een blauw bandje.")
            else:
                print("Je krijgt een rood bandje.")

        drink = ask_question("Wat wil je drinken?")

        if drink.lower() == "cola":
            bandje = ask_question("Heb je een bandje? (ja/nee)")

            if bandje.lower() == "ja":
                print("Astublieft, complimenten van het huis!")
            else:
                print(f"Asjeblieft, je {drink}. Dat is dan {PRIJS_COLA} euro.")
        elif drink.lower() == "bier":
            stempel_bandje = ask_question("Heb je een stempel of bandje? (ja/nee)")

            if stempel_bandje.lower() == "ja":
                print(f"Asjeblieft, je {drink}. Dat is dan {PRIJS_BIER} euro.")
            else:
                print("Sorry, je mag nog geen alcohol bestellen onder de 21.")
        elif drink.lower() == "champagne":
            if vip.lower() == "ja" and name.lower() in VIP_LIST:
                print(f"Astublieft, je {drink}. Dat is dan {PRIJS_CHAMPAGNE} euro.")
            else:
                print("Sorry, alleen VIPs mogen champagne bestellen.")
        else:
            kleur = "rood"
            print(f"Geen idee wat je bedoelt. Hier heb je een glaasje water. Je krijgt van mij een rood {kleur} bandje.")

if __name__ == "__main__":
    main()

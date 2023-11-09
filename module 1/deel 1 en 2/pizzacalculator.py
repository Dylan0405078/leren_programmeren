# Prijzen voor de verschillende pizzagroottes
PIZZA_PRIJZEN = {
    "small": 8.99,
    "medium": 12.99,
    "large": 15.99
}

# bestelling
def bereken_totaal(bestelling):
    TOTAAL = 0
    bonnetje = "\n==============================\n"
    bonnetje += "          UW BESTELLING\n"
    bonnetje += "==============================\n"
    
    for grootte, aantal in bestelling.items():
        prijs_per_pizza = PIZZA_PRIJZEN[grootte]
        totaal_per_grootte = prijs_per_pizza * aantal
        bonnetje += f"{aantal} {grootte.capitalize()} pizza('s)     ${prijs_per_pizza:.2f} per stuk     ${totaal_per_grootte:.2f}\n"
        TOTAAL += totaal_per_grootte

    bonnetje += "==============================\n"
    bonnetje += f"      TOTAALPRIJS: ${TOTAAL:.2f}\n"
    bonnetje += "==============================\n"

    return bonnetje

# Hoofdprogramma
if __name__ == "__main__":
    print("Welkom bij de Pizza Calculator!")
    
    bestelling = {}
    
    # aantal pizza's per grootte
    for grootte in PIZZA_PRIJZEN.keys():
        aantal = int(input(f"Hoeveel {grootte.capitalize()} pizza('s) wilt u bestellen? "))
        bestelling[grootte] = aantal
    
    # bonnetje printen
    bonnetje = bereken_totaal(bestelling)
    print(bonnetje)
PIZZA_PRIJZEN = {"small": 8.99, "medium": 12.99, "large": 15.99}

def bereken_totaal(bestelling):
    totaal = sum(PIZZA_PRIJZEN[grootte] * aantal for grootte, aantal in bestelling.items())
    bonnetje = "\n============================================================\n"
    bonnetje += "          UW BESTELLING\n"
    bonnetje += "============================================================\n"
    bonnetje += "\n".join(f"{aantal} {grootte.capitalize()} pizza('s)     ${PIZZA_PRIJZEN[grootte]:.2f} per stuk     ${PIZZA_PRIJZEN[grootte] * aantal:.2f}" for grootte, aantal in bestelling.items())
    bonnetje += "\n============================================================\n"
    bonnetje += f"      TOTAALPRIJS: ${totaal:.2f}\n"
    bonnetje += "============================================================\n"
    return bonnetje

def vraag_geheel_getal(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ongeldige invoer. Voer een geheel getal in.")

print("Welkom bij de Pizza Calculator!")
bestelling = {grootte: vraag_geheel_getal(f"Hoeveel {grootte.capitalize()} pizza('s) wilt u bestellen? ") for grootte in PIZZA_PRIJZEN.keys()}
print(bereken_totaal(bestelling))

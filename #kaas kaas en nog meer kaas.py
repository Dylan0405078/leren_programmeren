print("Welkom bij 'Wie ben ik? - Kaaseditie'!")

# Vraag of de kaas geel is
antwoord1 = input("Is de kaas geel? (ja/nee): ").lower()

if antwoord1 == "ja":
    # Vraag of er gaten in de kaas zitten
    antwoord2 = input("Zitten er gaten in? (ja/nee): ").lower()
    
    if antwoord2 == "ja":
        # Vraag of de kaas belachelijk duur is
        antwoord3 = input("Is de kaas belachelijk duur? (ja/nee): ").lower()
        
        if antwoord3 == "ja":
            print("Je bent een Emmenthaler kaas.")
        else:
            print("Je bent een Leerdammer kaas.")
    else:
        # Vraag of de kaas hard als steen is
        antwoord4 = input("Is de kaas hard als steen? (ja/nee): ").lower()
        
        if antwoord4 == "ja":
            print("Je bent een Parmigiano Reggiano kaas.")
        else:
            print("Je bent een Goudse kaas.")
else:
    # Vraag of de kaas blauwe schimmel heeft
    antwoord5 = input("Heeft de kaas blauwe schimmel? (ja/nee): ").lower()
    
    if antwoord5 == "ja":
        # Vraag of de kaas een korst heeft
        antwoord6 = input("Heeft de kaas een korst? (ja/nee): ").lower()
        
        if antwoord6 == "ja":
            print("Je bent een Blue de Rochbaron kaas.")
        else:
            print("Je bent een Foume d'Ambert kaas.")
    else:
        # Vraag of de kaas een korst heeft
        antwoord7 = input("Heeft de kaas een korst? (ja/nee): ").lower()
        
        if antwoord7 == "ja":
            print("Je bent een Camembert kaas.")
        else:
            print("Je bent een Mozzarella kaas.")


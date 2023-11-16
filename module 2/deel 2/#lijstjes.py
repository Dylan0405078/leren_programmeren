#lijstjes

# Vraag om het aantal lijstjes
aantal_lijstjes = int(input("Hoeveel lijstjes wil je genereren? "))

for i in range(aantal_lijstjes):
    # Vraag om de lengte van de lijst
    lijst_lengte = int(input(f"Voer de lengte in voor lijst {i + 1}: "))
    
    
    gegenereerde_lijst = list(range(i + 1, (i + 1) * lijst_lengte + 1, i + 1))
    
    # Toon de lijst
    print(f"Lijst {i + 1}: {gegenereerde_lijst}")

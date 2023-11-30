#m&ms deel 2

import random

# Lijst met beschikbare kleuren
kleuren = ['rood', 'blauw', 'groen', 'geel', 'bruin']

# Vraag de gebruiker om het aantal M&M's toe te voegen
aantal_mm = int(input("Hoeveel M&M's wil je toevoegen aan de zak? "))

# Vul de zak met M&M's
zak_met_mm = {}

for _ in range(aantal_mm):
    kleur = random.choice(kleuren)

    # Controleer of de kleur al in de zak zit
    if kleur in zak_met_mm:
        zak_met_mm[kleur] += 1
    else:
        zak_met_mm[kleur] = 1


print("\nZak met M&M's:")
for kleur, aantal in zak_met_mm.items():
    print(f"{kleur}: {aantal}")

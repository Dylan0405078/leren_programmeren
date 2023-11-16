#m&ms
import random

# Maak een Tuple met beschikbare kleuren
kleuren_tuple = ('oranje', 'blauw', 'groen', 'bruin')

aantal_mms = int(input("Hoeveel M&M's wil je toevoegen aan de zak? "))

zak_met_mms = [random.choice(kleuren_tuple) for _ in range(aantal_mms)]


hoeveelheid_per_kleur = {kleur: zak_met_mms.count(kleur) for kleur in kleuren_tuple}

# Toon de hoeveelheid van elke kleur in de zak met M&M's
print("Hoeveelheid van elke kleur in de zak met M&M's:")
for kleur, hoeveelheid in hoeveelheid_per_kleur.items():
    print(f"{kleur}: {hoeveelheid}")
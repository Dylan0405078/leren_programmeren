#opdracht 11
from fruitmand import fruitmand

# Lijst van beschikbare kleuren in de fruitmand
beschikbare_kleuren = set(item['color'] for item in fruitmand)


while True:
    gekozen_kleur = input("Kies een kleur uit de beschikbare kleuren: ").lower()
    
    if gekozen_kleur in beschikbare_kleuren:
        break
    else:
        print(f"De kleur {gekozen_kleur} zit niet in de fruitmand. Probeer opnieuw.")

# Bepaal het verschil tussen het aantal ronde en niet ronde vruchten van de gekozen kleur
aantal_ronde = sum(1 for item in fruitmand if item['color'] == gekozen_kleur and item['round'])
aantal_niet_ronde = sum(1 for item in fruitmand if item['color'] == gekozen_kleur and not item['round'])
verschil = abs(aantal_ronde - aantal_niet_ronde)

# Print het resultaat op basis van het verschil
if aantal_ronde > aantal_niet_ronde:
    print(f"Er zijn {verschil} meer ronde vruchten dan niet ronde vruchten in de kleur {gekozen_kleur}")
elif aantal_ronde < aantal_niet_ronde:
    print(f"Er zijn {verschil} minder ronde vruchten dan niet ronde vruchten in de kleur {gekozen_kleur}")
else:
    print(f"Er zijn {verschil} ronde vruchten en {verschil} niet ronde vruchten in de kleur {gekozen_kleur}")

#opdracht 12

from fruitmand import fruitmand

# Vertaal de Engelse kleurnamen naar Nederlands
kleuren_vertaling = {'green': 'groen', 'yellow': 'geel', 'orange': 'oranje', 'red': 'rood', 'brown': 'bruin'}

# Vind het fruit met de langste naam en vertaal de kleur naar Nederlands
fruit_met_langste_naam = max(fruitmand, key=lambda item: len(item['name']))

# Print de gewenste informatie met Nederlandse kleur
kleur_nederlands = kleuren_vertaling.get(fruit_met_langste_naam['color'], fruit_met_langste_naam['color'])
print(f"De '{fruit_met_langste_naam['name']}' (hoeveelheid letters: {len(fruit_met_langste_naam['name'])}) heeft {kleur_nederlands} kleur en een gewicht van {fruit_met_langste_naam['weight']} gram.")

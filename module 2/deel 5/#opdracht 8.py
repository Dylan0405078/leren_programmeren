#opdracht 8
from fruitmand import fruitmand

# druif verwijderen
fruitmand = [item for item in fruitmand if item['name'] != 'druif']

# Print de unieke kleuren
unique_colors = set(item['color'] for item in fruitmand)

for color in unique_colors:
    print(color)

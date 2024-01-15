#opdracht 6

from fruitmand import fruitmand

round_fruits = [item['name'] for item in fruitmand if item.get('round')]

for item in round_fruits:
    print(item)

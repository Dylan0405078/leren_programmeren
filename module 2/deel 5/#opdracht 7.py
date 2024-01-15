#opdracht 7

from fruitmand import fruitmand

#fruitmand.append({
    'name': 'watermeloen',
    'weight': 5000,  
    'color': 'green',
    'round': True
})


# Print the total weight of the fruitmand
total_weight = sum(item['weight'] for item in fruitmand)
print(f'{total_weight} gram')

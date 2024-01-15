#opdracht 5

from fruitmand_1 import fruitmand
appel_gewicht = next(item['weight'] for item in fruitmand if item['name'] == 'appel')
print(f'{appel_gewicht} gram')

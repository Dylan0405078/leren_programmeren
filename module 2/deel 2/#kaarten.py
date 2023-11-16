#kaarten


#deck.pop()


import itertools
import random

# maken een deck met 4 kleuren en 11 kaarten per kleur
kleuren = ['harten', 'klaveren', 'schoppen', 'ruiten']
kaarten = [str(i) for i in range(2, 11)] + ['boer', 'vrouw', 'heer', 'aas']
deck = list(itertools.product(kaarten, kleuren))

# 2 jokers toevoegen aan deck 
deck.extend([('joker', 'joker')])

random.shuffle(deck)

# Toon de 7 kaarten
print("Bovenste 7 kaarten:")
for kaart in deck[:7]:
    print(f"{kaart[0]} van {kaart[1]}")

# Overige kaarten
print("\nOverige kaarten in het deck:")
overige_kaarten = [f"{kaart[0]}  {kaart[1]}" for kaart in deck[7:]]
print(', '.join(overige_kaarten))

# Totaal aantal kaarten in het deck
totaal_aantal_kaarten = len(deck)
print(f'\nTotaal aantal kaarten in het deck: {totaal_aantal_kaarten}')

# Aantal kaarten zonder de eerste 7
aantal_overige_kaarten = len(deck) - 7
print(f'Aantal kaarten zonder de eerste 7: {aantal_overige_kaarten}')

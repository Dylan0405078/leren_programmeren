#kaarten
import itertools
import random

# Genereer een deck met 4 kleuren en 13 kaarten per kleur
kleuren = ['harten', 'klaveren', 'schoppen', 'ruiten']
kaarten = [str(i) for i in range(2, 11)] + ['boer', 'vrouw', 'heer', 'aas']
deck = list(itertools.product(kaarten, kleuren))

# Voeg 2 jokers toe aan het deck
deck.extend([('joker', 'joker')] * 2)

# Schud het deck
random.shuffle(deck)

# Toon de 7 kaarten
print("Bovenste 7 kaarten:")
for kaart in deck[:7]:
    print(f"{kaart[0]} van {kaart[1]}")

# Toon de overige kaarten als een opsomming
print("\nOverige kaarten in het deck:")
overige_kaarten = [f"{kaart[0]}  {kaart[1]}" for kaart in deck[7:]]
print(', '.join(overige_kaarten))

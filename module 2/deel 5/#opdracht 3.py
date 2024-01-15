#opdracht 3
import random
from fruitmand import fruitmand

# user input hoeveel stukjes fruit
num_prints = int(input("Hoeveel fruit wil je toevoegen? "))

# dictionary aanmaken om het fruit te tellen
fruit_counts = {}

# exporteren van unieke fruitsoorten
unique_fruits = set(item['name'] for item in fruitmand)

# fruit kiezen
for _ in range(num_prints):
    random_fruit = random.choice(list(unique_fruits))
    
    #count updaten fruit
    if random_fruit in fruit_counts:
        fruit_counts[random_fruit] += 1
    else:
        fruit_counts[random_fruit] = 1

# Print the counts of each fruit
print("\nCount of fruit:")
for fruit, count in fruit_counts.items():
    print(f"{fruit}: {count}")
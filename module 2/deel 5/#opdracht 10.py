#opdracht 10

from fruitmand import fruitmand

# Sort the fruit by weight in descending order
sorted_fruit = sorted(fruitmand, key=lambda item: item['weight'], reverse=True)

# Print names and weights in kilograms in descending order
for item in sorted_fruit:
    print(f"{item['name']}: {item['weight'] / 1000} kg")

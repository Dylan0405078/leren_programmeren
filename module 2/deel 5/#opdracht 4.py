#opdracht 4
from fruitmand import fruitmand

# Print each reversed fruit name on a new line
for name in reversed([item['name'] for item in fruitmand]):
    print(name)

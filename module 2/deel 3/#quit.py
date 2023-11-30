#quit

iterations = 0

while True:
    user_input = input('? ')
    iterations += 1

    if user_input.lower() == 'quit':
        break

print(f"Aantal iteraties: {iterations}")

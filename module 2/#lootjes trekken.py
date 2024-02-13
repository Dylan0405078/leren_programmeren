import random
import time
import os

print("Welkom bij het lootjes trekken programma!")

# Unieke namen verzamelen
deelnemers = set()
while len(deelnemers) < 3:
    naam = input("Voer een naam in: ")
    if naam not in deelnemers:
        deelnemers.add(naam)
    else:
        print("Deze naam is al ingevoerd. Probeer opnieuw.")

# Lootjes in een lijst zetten
deelnemers = list(deelnemers)

# Lootjes trekken
lootjes = list(deelnemers)
random.shuffle(lootjes)
while any(lootjes[i] == deelnemers[i] for i in range(len(lootjes))):
    random.shuffle(lootjes)

# Lootjes en namen tonen
while True:
    naam_vragen = input("Voer een naam in om het bijbehorende lootje te zien (of 'stop' om te eindigen): ")
    
    if naam_vragen.lower() == 'stop':
        print('Het programma word afgesloten.....')
        break

    try:
        index = deelnemers.index(naam_vragen)
        print(f"{naam_vragen} heeft lootje: {lootjes[index]}")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')  # Console leegmaken
    except ValueError:
        print(f"Ongeldige naam. Probeer opnieuw.")

time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')  # Console leegmaken

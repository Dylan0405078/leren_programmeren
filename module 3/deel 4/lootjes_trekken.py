import random
import time
import os

print("Welkom bij het lootjes trekken programma!")

# Verzamelen van namen en cadeauverzoeken
deelnemers_met_verzoeken = {}
while len(deelnemers_met_verzoeken) < 3:
    naam = input("Voer een naam in: ")
    if naam not in deelnemers_met_verzoeken:
        verzoeken = []
        for i in range(3):
            verzoek = input(f"Voer cadeauverzoek {i+1} in voor {naam}: ")
            verzoeken.append(verzoek)
        deelnemers_met_verzoeken[naam] = verzoeken
    else:
        print("Deze naam is al ingevoerd. Probeer opnieuw.")

# Lootjes trekken
deelnemers = list(deelnemers_met_verzoeken.keys())
lootjes = list(deelnemers)
random.shuffle(lootjes)
while any(lootjes[i] == deelnemers[i] for i in range(len(lootjes))):
    random.shuffle(lootjes)

# Lootjes en verzoeken tonen
while True:
    naam_vragen = input("Voer een naam in om het bijbehorende lootje en verzoeken te zien (of 'stop' om te eindigen): ")
    
    if naam_vragen.lower() == 'stop':
        print('Het programma wordt afgesloten.....')
        break

    if naam_vragen in deelnemers:
        index = deelnemers.index(naam_vragen)
        getrokken_naam = lootjes[index]
        verzoeken = deelnemers_met_verzoeken[getrokken_naam]
        print(f"{naam_vragen} heeft lootje: {getrokken_naam}")
        print("Verlanglijstje:")
        for i, verzoek in enumerate(verzoeken, start=1):
            print(f"  Cadeau {i}: {verzoek}")
    else:
        print(f"Ongeldige naam. Probeer opnieuw.")

    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')  # Console leegmaken

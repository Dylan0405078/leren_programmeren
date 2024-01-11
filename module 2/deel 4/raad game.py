import random

def raden_spel():
    geheim_getal = random.randint(1, 1000)
    score = 0
    ronden = 0

    while ronden < 20:
        raadbeurten = 0  # aparte teller voor raadbeurten in elke ronde
        while raadbeurten < 10:
            gok = input("Raad een getal tussen 1 en 1000 (of 'stop' om te eindigen): ")

            if gok.lower() == 'stop':
                return score  # teruggeven van de score zonder de ronde te verhogen

            try:
                gok = int(gok)
            except ValueError:
                print("Ongeldige invoer. Voer een geldig getal in.")
                continue

            raadbeurten += 1
            verschil = abs(geheim_getal - gok)

            if verschil < 20:
                print("Je bent heel warm!")
            elif verschil < 50:
                print("Je bent warm!")

            if gok == geheim_getal:
                score += 1
                print(f"Goed geraden! Je score is nu {score}")
                return score  # teruggeven van de score en de ronde beëindigen
            else:
                print("Hoger" if gok < geheim_getal else "Lager")

        print("Maximaal aantal pogingen bereikt. Het geheime getal was:", geheim_getal)
        break

    print(f"Ronde {ronden} is voorbij. Je score is nu {score}.\n")
    return score

def main():
    eindscore = 0

    for _ in range(20):
        doorgaan = input("Nog een getal raden? (ja/nee): ")
        if doorgaan.lower() != 'ja':
            break

        eindscore += raden_spel()

    print(f"\nEindscore: {eindscore}")

if __name__ == "__main__":
    main()

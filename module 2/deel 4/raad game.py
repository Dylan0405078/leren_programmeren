import random

def raden_spel():
    
    score = 0
    ronden = 1

    while ronden <= 20:
        geheim_getal = random.randint(1, 1000)
        raadbeurten = 0  

        while raadbeurten < 10:
            gok = input("Raad een getal tussen 1 en 1000 (of 'stop' om te eindigen): ")

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
                break
            else:
                print("Hoger" if gok < geheim_getal else "Lager")

        print("Maximaal aantal pogingen bereikt. Het geheime getal was:", geheim_getal)
        print(f"Ronde {ronden} is voorbij. Je score is nu {score}.\n")
        ronden += 1

        nog_een_keer = input("Wil je nog een getal raden? (ja/nee): ")
        if nog_een_keer.lower() != 'ja':
            return score, False  

def main():
    eindscore = 0
    doorgaan = 'ja'  

    for _ in range(20):
        if doorgaan == 'ja':
            doorgaan = input("Wil je een getal raden? (ja/nee): ")

        if doorgaan.lower() != 'ja':
            break

        score, doorgaan = raden_spel()
        eindscore += score

        if not doorgaan:
            break

    print(f"\nEindscore: {eindscore}")

if __name__ == "__main__":
    main()

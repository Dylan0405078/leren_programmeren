#order bug vervangen
def vraag_getal(volgorde):
    antwoord = input("Voer het " + volgorde + " getal in: ")
    getal = int(antwoord)
    return getal

def deel_getallen(a, b):
    if b == 0:
        print("Kan niet delen door 0")
        return None
    return a / b

getal_1 = vraag_getal("eerste")
getal_2 = int(input("Voer het tweede getal in: "))

if getal_2 == 0:
    print("Kan niet delen door 0")
else:
    resultaat = deel_getallen(getal_1, getal_2)
    if resultaat is not None:
        print("{} gedeeld door {} is gelijk aan {}".format(getal_1, getal_2, resultaat))

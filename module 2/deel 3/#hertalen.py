#hertalen
def hertalingsprogramma(tekst, vertaalwoorden):
    woordenlijst = tekst.split()
    nieuwe_tekst = ""

    for woord in woordenlijst:
        if woord.lower() in vertaalwoorden:
            nieuwe_tekst += vertaalwoorden[woord.lower()] + " "
        else:
            nieuwe_tekst += woord + " "

    return nieuwe_tekst.strip()

# vijf eigen woorden vertalen
hertalingen = {
    "een": "dit",
    "gehaktbal": "is",
    "is": "mijn",
    "erg": "hertaalprogramma",
    "lekker": ":)",
}

# vraag de gebruiker om 5 woorden in te vullen
originele_tekst = input("Voer een stukje tekst in (5 woorden) : ")

hertaalde_tekst = hertalingsprogramma(originele_tekst, hertalingen)

print("\nHertaalde tekst:")
print(hertaalde_tekst)

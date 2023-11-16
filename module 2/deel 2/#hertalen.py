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

# Verzin minimaal 5 woorden om te hertalen
hertalingen = {
    "een": "dit",
    "gehaktbal": "is",
    "is": "mijn",
    "erg": "hertaalprogramma",
    "lekker": ":)",
}

# Vraag de gebruiker om een stukje tekst
originele_tekst = input("Voer een stukje tekst in: ")

# Voer het hertalingsprogramma uit
hertaalde_tekst = hertalingsprogramma(originele_tekst, hertalingen)

# Print de hertaalde tekst
print("\nHertaalde tekst:")
print(hertaalde_tekst)

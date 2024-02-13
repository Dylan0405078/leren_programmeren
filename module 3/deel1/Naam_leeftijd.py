def vraag_persoonlijke_info():
    naam = input("Wat is je naam? ")
    leeftijd = input("Hoe oud ben je? ")
    woonplaats = input("Waar woon je? ")
    return {'name': naam, 'age': leeftijd, 'city': woonplaats}

def verzamel_gebruikersgegevens():
    gebruikers = []
    while True:
        stop_input = input("Toets enter om door te gaan of stop om te printen: ")
        if stop_input.lower() == 'stop':
            break
        gebruikers.append(vraag_persoonlijke_info())
    return gebruikers




 
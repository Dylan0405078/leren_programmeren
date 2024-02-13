from Naam_leeftijd import verzamel_gebruikersgegevens


gebruikers_info = verzamel_gebruikersgegevens()

for gebruiker in gebruikers_info:
    print(f"In {gebruiker['city']} woont de {gebruiker['age']} jarige {gebruiker['name']}.")

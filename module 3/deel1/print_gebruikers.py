from Naam_leeftijd import verzamel_gebruikersgegevens

gebruikers_info = verzamel_gebruikersgegevens()

for gebruiker in gebruikers_info:
    print(f"{gebruiker['name']}, die in {gebruiker['city']} woont, is {gebruiker['age']} jaar oud.")


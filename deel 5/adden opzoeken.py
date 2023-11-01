def get_value(data: str, separator: str, position: int) -> str:
    # Split de gegeven data op basis van de opgegeven separator
    splitted_strings = data.split(separator)
    
    # Controleer of de opgegeven positie geldig is
    if 0 <= position < len(splitted_strings):
        # Haal de waarde op die overeenkomt met de opgegeven positie
        value = splitted_strings[position]
        return value
    else:
        # Als de positie buiten het bereik ligt, retourneer een lege string
        return "vul een geldig ID in!"



data = 'muis,kat,hond,vogel,vis'
separator = ','
position = 4
result = get_value(data, separator, position)
print(result)  
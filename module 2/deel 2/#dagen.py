#dagen

# Maak een Tuple met dagen van de week
dagen_van_de_week = ('maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag')

# Toon alle dagen van de week
print("Alle dagen van de week zijn:", ', '.join(dagen_van_de_week))

# Toon de werkdagen
werkdagen = dagen_van_de_week[:5]
print("De werkdagen zijn:", ', '.join(werkdagen))

# Toon de weekenddagen
weekenddagen = dagen_van_de_week[5:]
print("De weekenddagen zijn:", ', '.join(weekenddagen))

# Toon alle dagen van de week in omgekeerde volgorde
print("Alle dagen van de week in omgekeerde volgorde zijn:", ', '.join(reversed(dagen_van_de_week)))

# Toon de werkdagen in omgekeerde volgorde
print("De werkdagen in omgekeerde volgorde zijn:", ', '.join(reversed(werkdagen)))

# Toon de weekenddagen in omgekeerde volgorde
print("De weekenddagen in omgekeerde volgorde zijn:", ', '.join(reversed(weekenddagen)))

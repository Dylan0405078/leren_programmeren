#dagen

# Maak een Tuple met dagen van de week
dagen_van_de_week = ('maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag')


print("Alle dagen van de week zijn:", ', '.join(dagen_van_de_week))

werkdagen = dagen_van_de_week[:5]
print("De werkdagen zijn:", ', '.join(werkdagen))

weekenddagen = dagen_van_de_week[5:]
print("De weekenddagen zijn:", ', '.join(weekenddagen))

print("Alle dagen van de week in omgekeerde volgorde zijn:", ', '.join(reversed(dagen_van_de_week)))

print("De werkdagen in omgekeerde volgorde zijn:", ', '.join(reversed(werkdagen)))

print("De weekenddagen in omgekeerde volgorde zijn:", ', '.join(reversed(weekenddagen)))

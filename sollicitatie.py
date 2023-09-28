#sollicitatie



# Definieer constanten voor de vereisten
MIN_GEWICHT = 90  # Minimaal gewicht in kg
MAX_GEWICHT = 120  # Maximaal gewicht in kg
MIN_LENGTE = 150  # Minimale lengte in cm
MAX_LENGTE = 220  # Maximale lengte in cm
MIN_DIEREN_ERVARING = 4  # Minimale jaren ervaring met dieren-dressuur
MIN_JONGLEREN_ERVARING = 5  # Minimale jaren ervaring met jongleren
MIN_ACROBATIEK_ERVARING = 3  # Minimale jaren ervaring met acrobatiek

# Vraag alle benodigde informatie aan de kandidaat
vrachtwagen_rijbewijs = input("Heeft u een geldig Vrachtwagen rijbewijs? (ja/nee): ").strip().lower()
hoge_hoed = input("Heeft u een hoge hoed? (ja/nee): ").strip().lower()
lichaamsgewicht = float(input("Wat is uw lichaamsgewicht in kg?: "))
lichaamslengte = float(input("Wat is uw lichaamslengte in cm?: "))
dieren_erf = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?: "))
jongleren_erf = int(input("Hoeveel jaar ervaring heeft u met jongleren?: "))
acrobatiek_erf = int(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek?: "))

# Beoordeel de geschiktheid van de kandidaat
geschikt = (
    vrachtwagen_rijbewijs == "ja" and
    hoge_hoed == "ja" and
    MIN_GEWICHT < lichaamsgewicht < MAX_GEWICHT and
    MIN_LENGTE < lichaamslengte < MAX_LENGTE and
    (dieren_erf >= MIN_DIEREN_ERVARING or jongleren_erf >= MIN_JONGLEREN_ERVARING or acrobatiek_erf >= MIN_ACROBATIEK_ERVARING)
)

# Geef de uitslag van de sollicitatie
if geschikt:
    print("U mag solliciteren naar de functie van circusdirecteur!")
else:
    print("U voldoet niet aan alle vereisten om te solliciteren naar de functie van circusdirecteur.")
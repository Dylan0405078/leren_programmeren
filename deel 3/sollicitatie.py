#sollicitatie


#  constanten voor de initiële vereisten
MIN_GEWICHT = 90  # Minimaal gewicht in kg
MAX_GEWICHT = 120  # Maximaal gewicht in kg
MIN_LENGTE = 150  # Minimale lengte in cm
MAX_LENGTE = 220  # Maximale lengte in cm
MIN_DIEREN_ERVARING = 4  # Minimale jaren ervaring met dieren-dressuur
MIN_JONGLEREN_ERVARING = 5  # Minimale jaren ervaring met jongleren
MIN_ACROBATIEK_ERVARING = 3  # Minimale jaren ervaring met acrobatiek
MIN_ONDERNEMERS_JAREN = 3 # Minimale jaren in de onderneming
MIN_WERKNEMERS = 5 # Minimale hoeveelheid werknemers
MIN_SNOR_BREEDTE = 10 # Minimale snor breedte
MIN_KRULHAAR_LENGTE = 20 # minimale lengte haar
MIN_GLIMLACH_BREEDTE = 10 # minimale glimlach breedte

# Vraag alle benodigde informatie aan de kandidaat voor de initiële vereisten
vrachtwagen_rijbewijs = input("Heeft u een geldig Vrachtwagen rijbewijs? (ja/nee): ").strip().lower()
hoge_hoed = input("Heeft u een hoge hoed? (ja/nee): ").strip().lower()
lichaamsgewicht = float(input("Wat is uw lichaamsgewicht in kg?: "))
lichaamslengte = float(input("Wat is uw lichaamslengte in cm?: "))
dieren_erf = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?: "))
jongleren_erf = int(input("Hoeveel jaar ervaring heeft u met jongleren?: "))
acrobatiek_erf = int(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek?: "))

# Beoordeel de geschiktheid van de kandidaat voor de initiële vereisten
geschikt_initieel = (
    vrachtwagen_rijbewijs == "ja" and
    hoge_hoed == "ja" and
    MIN_GEWICHT < lichaamsgewicht < MAX_GEWICHT and
    MIN_LENGTE < lichaamslengte < MAX_LENGTE and
    (dieren_erf >= MIN_DIEREN_ERVARING or jongleren_erf >= MIN_JONGLEREN_ERVARING or acrobatiek_erf >= MIN_ACROBATIEK_ERVARING)
)


# Vraag alle benodigde informatie aan de kandidaat voor de nieuwe vereisten
diploma_ondernemen = input("Heeft u een Diploma MBO-4 ondernemen? (ja/nee): ").strip().lower()
ondernemer_jaren = int(input("Hoeveel jaar bent u al ondernemer?: "))
werknemers_in_loondienst = int(input("Hoeveel werknemers heeft u in loondienst?: "))
geslacht = input("Wat is uw geslacht? (man/vrouw/anders): ").strip().lower()

# Beoordeel de geschiktheid van de kandidaat voor de nieuwe vereisten
geschikt_nieuw = False

if (
    (diploma_ondernemen == "ja") or
    (ondernemer_jaren > MIN_ONDERNEMERS_JAREN and werknemers_in_loondienst >= MIN_WERKNEMERS)
):
    if (
        (geslacht == "man" and input("Heeft u een snor? (ja/nee): ").strip().lower() == "ja" and
         float(input("Hoe breed is uw snor in cm?: ")) > MIN_SNOR_BREEDTE) or
        (geslacht == "vrouw" and input("Heeft u rood krulhaar? (ja/nee): ").strip().lower() == "ja" and
         float(input("Hoe lang is uw rood krulhaar in cm?: ")) > MIN_KRULHAAR_LENGTE) or
        (geslacht == "anders" and
         float(input("Hoe breed is uw glimlach in cm?: ")) > MIN_GLIMLACH_BREEDTE)
    ):
        geschikt_nieuw = True

# Beoordeel de totale geschiktheid van de kandidaat
geschikt_totaal = geschikt_initieel and geschikt_nieuw

# Maak een lijst met criteria waaraan niet is voldaan
criteria_niet_voldaan = []

if not vrachtwagen_rijbewijs == "ja":
    criteria_niet_voldaan.append("Geldig Vrachtwagen rijbewijs")

if not hoge_hoed == "ja":
    criteria_niet_voldaan.append("Hoge hoed")

if not (MIN_GEWICHT < lichaamsgewicht < MAX_GEWICHT):
    criteria_niet_voldaan.append("Geldig lichaamsgewicht")

if not (MIN_LENGTE < lichaamslengte < MAX_LENGTE):
    criteria_niet_voldaan.append("Geldig lichaamslengte")

if not (dieren_erf >= MIN_DIEREN_ERVARING or jongleren_erf >= MIN_JONGLEREN_ERVARING or acrobatiek_erf >= MIN_ACROBATIEK_ERVARING):
    criteria_niet_voldaan.append("Ervaring met dieren-dressuur, jongleren of acrobatiek")

if not (diploma_ondernemen == "ja" or (ondernemer_jaren > MIN_ONDERNEMERS_JAREN and werknemers_in_loondienst >= MIN_WERKNEMERS)):
    criteria_niet_voldaan.append("Diploma MBO-4 ondernemen of ondernemerservaring met minimaal 5 werknemers in loondienst")

if geslacht == "man" and not (input("Heeft u een snor? (ja/nee): ").strip().lower() == "ja" and float(input("Hoe breed is uw snor in cm?: ")) > MIN_SNOR_BREEDTE):
    criteria_niet_voldaan.append("Snor breder dan 10 cm")

if geslacht == "vrouw" and not (input("Heeft u rood krulhaar? (ja/nee): ").strip().lower() == "ja" and float(input("Hoe lang is uw rood krulhaar in cm?: ")) > MIN_KRULHAAR_LENGTE):
    criteria_niet_voldaan.append("Rood krulhaar langer dan 20 cm")

if geslacht == "anders" and not (float(input("Hoe breed is uw glimlach in cm?: ")) > MIN_GLIMLACH_BREEDTE):
    criteria_niet_voldaan.append("Brede glimlach breder dan 10 cm")

# Geef de uitslag van de sollicitatie
if geschikt_totaal:
    print("U mag solliciteren naar de functie van circusdirecteur!")
else:
    print("U voldoet niet aan alle vereisten om te solliciteren naar de functie van circusdirecteur.")
    print("Criteria waaraan niet is voldaan:")
    for criteria in criteria_niet_voldaan:
        print(criteria)
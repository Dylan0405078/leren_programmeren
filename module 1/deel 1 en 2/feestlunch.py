
AANTAL_CROISSANTJES = 17
PRIJS_PER_CROISSANT = 0.39


AANTAL_STOKBRODEN = 2
PRIJS_PER_STOKBROOD = 2.78


AANTAL_KORTINGSBONNEN = 3
WAARDE_PER_BON = 0.50

kosten_croissantjes = AANTAL_CROISSANTJES * PRIJS_PER_CROISSANT

kosten_stokbroden = AANTAL_STOKBRODEN * PRIJS_PER_STOKBROOD

korting_kortingsbonnen = AANTAL_KORTINGSBONNEN * WAARDE_PER_BON


totaal_zonder_korting = kosten_croissantjes + kosten_stokbroden

totaal_met_korting = totaal_zonder_korting - korting_kortingsbonnen

print(f"De feestlunch kost bij de bakker {totaal_met_korting} voor de {AANTAL_STOKBRODEN} stokbroden en {AANTAL_CROISSANTJES} croissantjes als de {AANTAL_KORTINGSBONNEN} kortingsbonnen nog geldig zijn!")

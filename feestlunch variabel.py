aantal_croissatjes = int(input("hoeveel croissants heb je?"))
PRIJS_PER_CROISSANT = 0.39


aantal_stokbroden = int(input("hoeveel stokbroden heb je?"))
PRIJS_PER_STOKBROOD = 2.78


aantal_kortingsbonnen = int(input("hoeveel kortingsbonnen heb je?"))
WAARDE_PER_BON = 0.50

kosten_croissantjes = aantal_croissatjes * PRIJS_PER_CROISSANT

kosten_stokbroden = aantal_stokbroden * PRIJS_PER_STOKBROOD

korting_kortingsbonnen = aantal_kortingsbonnen * WAARDE_PER_BON


totaal_zonder_korting = kosten_croissantjes + kosten_stokbroden

totaal_met_korting = totaal_zonder_korting - korting_kortingsbonnen

print(f"De feestlunch kost bij de bakker {totaal_met_korting} voor de {aantal_stokbroden} stokbroden en {aantal_croissatjes} croissantjes als de {aantal_kortingsbonnen} kortingsbonnen nog geldig zijn!")

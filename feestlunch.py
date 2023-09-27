
aantal_croissantjes = 17
prijs_per_croissant = 0.39


aantal_stokbroden = 2
prijs_per_stokbrood = 2.78


aantal_kortingsbonnen = 3
waarde_per_bon = 0.50

#  kosten van de croissantjes
kosten_croissantjes = aantal_croissantjes * prijs_per_croissant

# totale kosten van de stokbroden
kosten_stokbroden = aantal_stokbroden * prijs_per_stokbrood

#  totale korting van de kortingsbonnen
korting_kortingsbonnen = aantal_kortingsbonnen * waarde_per_bon

#  totale kosten zonder korting
totaal_zonder_korting = kosten_croissantjes + kosten_stokbroden

#  uiteindelijke kosten na aftrek van de kortingsbonnen
totaal_met_korting = totaal_zonder_korting - korting_kortingsbonnen

print(f"De feestlunch kost bij de bakker {totaal_met_korting} voor de {aantal_stokbroden} stokbroden en {aantal_croissantjes} croissantjes als de {aantal_kortingsbonnen} kortingsbonnen nog geldig zijn!")

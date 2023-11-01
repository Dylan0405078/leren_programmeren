#test file defs
from defs import *




#cilinder
diameter = 8  # Vul de gewenste diameter in
hoogte = 7   # Vul de gewenste hoogte in

inhoud_cilinder = calculate_cilinder_content(diameter, hoogte)
print(f"De inhoud van de cilinder is {inhoud_cilinder} ml")

#afronden op 5 centen

original_amount = 17.17
rounded_amount = round_to_nearest(original_amount)
print(f"{original_amount:.2f} wordt afgerond naar {rounded_amount:.2f}")



#korting scooters

price = 600.0
brand = 'Vespa'
discount = calc_discount(price, brand, month_discount_brands)
print(f"Korting voor {brand}: {discount:.2f} euro")

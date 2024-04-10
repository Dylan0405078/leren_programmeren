from recipe import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')

# -------- INPUT --------
nr_persons = input_nr_persons("Voer het aantal personen in: ")

# ----- BEREKENINGEN ----
# Calculate factor
factor = nr_persons / RECIPE_PERSONS

# Adjust quantities
eggs_quantity = AMOUNT_EGGS * factor
milk_quantity = AMOUNT_MILK * factor
salt_quantity = AMOUNT_SALT * factor
pepper_quantity = AMOUNT_PEPPER * factor
oil_quantity = AMOUNT_OIL * factor
onions_quantity = AMOUNT_ONIONS * factor
garlics_quantity = AMOUNT_GARLICS * factor
paprikas_quantity = AMOUNT_PAPRIKAS * factor
spinach_quantity = AMOUNT_SPINACH * factor
cheese_quantity = AMOUNT_CHEESE * factor







# Round the quantities appropriately
amount_eggs = round_piece(amount_eggs)
amount_milk = round_quarter(amount_milk)
amount_salt = round_quarter(amount_salt)
amount_pepper = round_quarter(amount_pepper)
amount_oil = round_quarter(amount_oil)
amount_onions = round_piece(amount_onions)
amount_garlics = round_piece(amount_garlics)
amount_paprikas = round_piece(amount_paprikas)
amount_spinach = round_quarter(amount_spinach)
amount_cheese = round_quarter(amount_cheese)

# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} {str_single_plural(nr_persons, TXT_PERSONS)}:')
print('-----------------------------------------------')
# print (formatted) all amounts and units combined with their ingrediënt descriptions

print(f"{str_amount_fraction(eggs_quantity)} {str_units(eggs_quantity, UNIT_EGGS)} {str_single_plural(eggs_quantity, TXT_EGGS)}")
print(f"{str_amount_fraction(milk_quantity)} {str_units(milk_quantity, UNIT_MILK)} {str_single_plural(milk_quantity, TXT_MILK)}")
print(f"{str_amount_fraction(salt_quantity)} {str_units(salt_quantity, UNIT_SALT)} {str_single_plural(salt_quantity, TXT_SALT)}")
print(f"{str_amount_fraction(pepper_quantity)} {str_units(pepper_quantity, UNIT_PEPPER)} {str_single_plural(pepper_quantity, TXT_PEPPER)}")
print(f"{str_amount_fraction(oil_quantity)} {str_units(oil_quantity, UNIT_OIL)} {str_single_plural(oil_quantity, TXT_OIL)}")
print(f"{str_amount_fraction(onions_quantity)} {str_units(onions_quantity, UNIT_ONIONS)} {str_single_plural(onions_quantity, TXT_ONIONS)}")
print(f"{str_amount_fraction(garlics_quantity)} {str_units(garlics_quantity, UNIT_GARLICS)} {str_single_plural(garlics_quantity, TXT_GARLICS)}")
print(f"{str_amount_fraction(paprikas_quantity)} {str_units(paprikas_quantity, UNIT_PAPRIKAS)} {str_single_plural(paprikas_quantity, TXT_PAPRIKAS)}")
print(f"{str_amount_fraction(spinach_quantity)} {str_units(spinach_quantity, UNIT_SPINACH)} {str_single_plural(spinach_quantity, TXT_SPINACH)}")
print(f"{str_amount_fraction(cheese_quantity)} {str_units(cheese_quantity, UNIT_CHEESE)} {str_single_plural(cheese_quantity, TXT_CHEESE)}")

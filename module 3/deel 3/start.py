import math
import time
import os
from constant import *
from functions import *


# invoer voor aantal personen
print('=========================Frittata recept=========================')
print("Hoeveel personen moeten er eten?")
nr_persons = input_nr_persons("Voer het aantal personen in: ")

# Ingrediënten voor het recept (4 personen)
eggs_quantity = adjust_quantity(7, nr_persons)
milk_quantity = adjust_quantity(0.5, nr_persons)
salt_quantity = adjust_quantity(0.5, nr_persons)
pepper_quantity = round(adjust_quantity(0.25, nr_persons), 1)
oil_quantity = adjust_quantity(1, nr_persons)
onions_quantity = adjust_quantity(1, nr_persons)
garlics_quantity = adjust_quantity(2, nr_persons)
paprikas_quantity = adjust_quantity(3, nr_persons)
spinach_quantity = adjust_quantity(1, nr_persons)
cheese_quantity = adjust_quantity(0.5, nr_persons)


# Uitvoer van aangepaste ingrediëntenlijst
print('=========================Frittata recept=========================')
print(f"recept voor: {nr_persons} personen")
print('-----------------------------------------------------------------')
print(f"{str_amount_fraction(eggs_quantity)} {str_units(eggs_quantity, UNIT_PIECES)} {str_single_plural(eggs_quantity, TXT_EGGS)}")
print(f"{str_amount_fraction(milk_quantity)} {str_units(milk_quantity, UNIT_CUPS)} {str_single_plural(milk_quantity, TXT_MILK)} ({unit2ml(milk_quantity, UNIT_CUPS)} mL)")
print(f"{str_amount_fraction(salt_quantity)} {str_units(salt_quantity, UNIT_TEASPOONS)} {str_single_plural(salt_quantity, TXT_SALT)} ({ml2gram(unit2ml(salt_quantity, UNIT_TEASPOONS), GRAM_PER_ML_SALT)} gram)")
print(f"{str_amount_fraction(pepper_quantity)} {str_units(pepper_quantity, UNIT_TEASPOONS)} {str_single_plural(pepper_quantity, TXT_PEPPER)} ({ml2gram(unit2ml(pepper_quantity, UNIT_TEASPOONS), GRAM_PER_ML_PEPPER)} gram)")
print(f"{str_amount_fraction(oil_quantity)} {str_units(oil_quantity, UNIT_SPOONS)} {str_single_plural(oil_quantity, TXT_OIL)} ({unit2ml(oil_quantity, UNIT_SPOONS)} mL)")
print(f"{str_amount_fraction(onions_quantity)} {str_units(onions_quantity, UNIT_PIECES)} {str_single_plural(onions_quantity, TXT_ONIONS)}")
print(f"{str_amount_fraction(garlics_quantity)} {str_units(garlics_quantity, UNIT_PIECES)} {str_single_plural(garlics_quantity, TXT_GARLICS)}")
print(f"{str_amount_fraction(paprikas_quantity)} {str_units(paprikas_quantity, UNIT_PIECES)} {str_single_plural(paprikas_quantity, TXT_PAPRIKAS)}")
print(f"{str_amount_fraction(spinach_quantity)} {str_units(spinach_quantity, UNIT_CUPS)} {str_single_plural(spinach_quantity, TXT_SPINACH)} ({ml2gram(unit2ml(spinach_quantity, UNIT_CUPS), GRAM_PER_ML_SPINACH)} gram)")
print(f"{str_amount_fraction(cheese_quantity)} {str_units(cheese_quantity, UNIT_CUPS)} {str_single_plural(cheese_quantity, TXT_CHEESE)} ({ml2gram(unit2ml(cheese_quantity, UNIT_CUPS), GRAM_PER_ML_CHEESE)} gram)")
print('=================================================================')

from constant import *
import math

def input_nr_persons(prompt: str) -> int:
    while True:
        try:
            nr_persons = int(input(prompt))
            if nr_persons > 0:
                return nr_persons
            print('getal moet groter zijn dan 0')
        except ValueError:
            print('Voer een geldig geheel getal in!')


def str_units(amount: float, unit: str) -> str:
    unit_parts = unit.split('|')
    if len(unit_parts) >= 2:
        return unit_parts[1] if amount >= 2 else ''
    else:
        return ''  


# Returns single or plural description of a string 'single description|plural description'
# depending on amount
def str_single_plural(amount: float, txt: str) -> str:
    description = txt.split('|')
    if amount == 1:
        return description[0]
    else:
        return description[1]


# Returns amount in string with ¼ , ½  and ¾
TXT_FRACTIONS = ('', '¼', '½', '¾')


def str_amount_fraction(amount: float) -> str:
    ints = int(amount)
    fraction = round(amount - ints, 2)
    quarter = round(fraction / 0.25)
    str_ints = str(ints) if ints > 0 else ''
    if fraction == 0:
        return str_ints
    else:
        return f"{str_ints} {TXT_FRACTIONS[quarter]}"


# Omrekenen van aantal personen
def adjust_quantity(amount: float, nr_persons: int) -> float:
    return (amount * nr_persons / 4)


#  aantal eenheden naar milliliter
def unit2ml(amount: float, unit: str) -> float:
    if unit == UNIT_SPOONS:
        return amount * ML_SPOON
    elif unit == UNIT_TEASPOONS:
        return amount * ML_TEASPOON
    elif unit == UNIT_CUPS:
        return amount * ML_CUP
    else:
        raise TypeError("Ongeldige eenheid!")


#  milliliter naar gram
def ml2gram(amount_ml: float, gram_per_ml: float) -> float:
    return amount_ml * gram_per_ml
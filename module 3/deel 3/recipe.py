import math

UNIT_PIECES = 'piece'
UNIT_SPOONS = 'spoon'
UNIT_TEASPOONS = 'teaspoon'
UNIT_CUPS = 'cup'

TXT_PIECES = '|'
TXT_SPOONS = 'eetlepel|eetlepels'
TXT_TEASPOONS = 'theelepel|theelepels'
TXT_CUPS = 'kopje|kopjes'

# Failsafe input of a number of persons
def input_nr_persons(prompt: str) -> int:
    while True:
        try:
            nr_persons = int(input(prompt))
            if nr_persons > 0: 
                return nr_persons
            print('getal moet groter zijn dan 0')
        except ValueError:
            print('Voer een geldig geheel getal in!')


# Returns single or plural description of a string 'single description|plural description' 
# depending on amount
def str_single_plural(amount: float, txt: str) -> str:
    description = txt.split('|')
    return description[0] if amount == 1 else description[1]


# Returns description of single or plural units
def str_units(amount: float, unit: str) -> str:
    if amount == 1:
        return unit.split('|')[0]
    else:
        return unit.split('|')[1]


# Returns amount in string with 1/4 or 1/2 or 3/4
TXT_FRACTIONS = ('','¼','½','¾')
def str_amount_fraction(amount: float) -> str:  
    amount = math.ceil(amount) 
    ints = int(amount)
    quarter = int((amount - ints) / 0.25)
    str_ints = str(ints) if ints > 0 else ''
    return str_ints + TXT_FRACTIONS[quarter]


# Units in ml
ML_SPOON = 15 # One spoon contains 15 ml
ML_TEASPOON = 5 # One teaspoon contains 5 ml
ML_CUP = 240 # One cup contains 240 ml

# Average densities in gram per ml for common ingredients, to calculate weight(gram) from milliliters(ml)
GRAM_PER_ML_SALT = 1.2
GRAM_PER_ML_PEPPER = 0.3
GRAM_PER_ML_CHEESE = 0.45
GRAM_PER_ML_SPINACH = 0.15

# Returns amount in gram for amount in milliliter based on density (weight per volume)
def ml2gram(amount_ml: float, gram_per_ml: float) -> float:
    return amount_ml * gram_per_ml

#defs
import math



#inhoud cilinder


def calculate_cilinder_content(diameter, hoogte):
    straal = diameter / 2
    inhoud = math.pi * straal ** 2 * hoogte
    afgeronde_inhoud = round(inhoud, 1)
    return afgeronde_inhoud





# afronden op 5 centen


def round_to_nearest(amount, rounding_value=0.05):
    
    
    remainder = amount % rounding_value
    if remainder < rounding_value / 2:
        return amount - remainder
    else:
        return amount + (rounding_value - remainder)




#korting scooters
month_discount_brands = 'Vespa,Kymco,Yamama'
MONTH_DISCOUNT_PERC = 10

def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
   
    discount_brands = set(month_discount_brands.split(','))

    if brand in discount_brands:
        
        discount = round((price * MONTH_DISCOUNT_PERC) / 100, 2)
    else:
        
        discount = 0.0

    return discount




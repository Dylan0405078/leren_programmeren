# functions.py
import data

def welcome_message():
    print("Welkom bij onze ijssalon!")
    print("Laten we beginnen met het samenstellen van je bestelling.")
    print("------------------------------")

def validate_input(prompt, valid_inputs):
    while True:
        user_input = input(prompt).strip().upper()
        if user_input in valid_inputs:
            return user_input
        else:
            print("Ongeldige invoer. Probeer het opnieuw.")

def order_summary(order):
    print("Je bestelling:")
    for item in order:
        if item.get('liters'):
            liters = item['liters']
            flavors = item['flavors']
            print(f"- {liters} liter(s) met smaken: {', '.join(flavors)}")
        else:
            scoops = item['scoops']
            cone_or_cup = item['type']
            flavors = item['flavors']
            topping = item['topping']
            print(f"- {scoops} bolletjes in een {cone_or_cup} met smaken: {', '.join(flavors)} en topping: {topping}")

def print_receipt(order, customer_type):
    total_cost = 0
    if customer_type == '2':  # Zakelijke klant
        print("\nBonnetje (Zakelijke klant):")
        print("-------------------------------")
        for item in order:
            for flavor, count in item['flavors'].items():
                print(f"{flavor.capitalize()}     x{count} liter = €{count * data.LITER_PRICE:.2f}")
            total_cost += item['total_price']
        print("-------------------------------")
        print(f"Totaal                 = €{total_cost:.2f}")
        print(f"BTW (9%)               = €{total_cost * data.BTW_RATE:.2f}")
        print("-------------------------------")
        print(f"Totaal inclusief BTW   = €{total_cost * (1 + data.BTW_RATE):.2f}")
    else:
        total_scoops = sum(item['scoops'] for item in order)
        total_cones = sum(1 for item in order if item['type'] == 'hoorntje')
        total_cups = sum(1 for item in order if item['type'] == 'bakje')
        total_cost = (
            total_scoops * data.SCOOP_PRICE + 
            total_cones * data.CONE_PRICE + 
            total_cups * data.CUP_PRICE
        )

        flavor_count = {}
        for item in order:
            for flavor in item['flavors']:
                if flavor in flavor_count:
                    flavor_count[flavor] += 1
                else:
                    flavor_count[flavor] = 1

        total_topping_cost = 0
        for item in order:
            if item['topping'] == 'slagroom':
                total_topping_cost += data.SLAGROOM_PRICE
            elif item['topping'] == 'sprinkels':
                total_topping_cost += item['scoops'] * data.SPRINKELS_PRICE
            elif item['topping'] == 'caramel saus':
                if item['type'] == 'hoorntje':
                    total_topping_cost += data.CARAMEL_SAUS_CONE_PRICE
                elif item['type'] == 'bakje':
                    total_topping_cost += data.CARAMEL_SAUS_CUP_PRICE

        total_cost += total_topping_cost

        print("\nBonnetje:")
        print("-------------------------------")
        for flavor, count in flavor_count.items():
            print(f"{flavor.capitalize()}     x{count}  = €{count * data.SCOOP_PRICE:.2f}")
        if total_cones > 0:
            print(f"Hoorntjes     x{total_cones}  = €{total_cones * data.CONE_PRICE:.2f}")
        if total_cups > 0:
            print(f"Bakjes        x{total_cups}  = €{total_cups * data.CUP_PRICE:.2f}")
        if total_topping_cost > 0:
            print(f"Toppings              = €{total_topping_cost:.2f}")
        print("-------------------------------")
        print(f"Totaal                 = €{total_cost:.2f}")
    print("-------------------------------")
    print("Bedankt voor je bezoek!")

def get_order_confirmation():
    return data.confirmation_message

def get_number_of_scoops():
    return data.scoops_message

def get_cone_or_cup(num_scoops):
    if num_scoops <= 3:
        return validate_input(data.cone_cup_message, ["HOORNTJE", "BAKJE"]).lower()
    else:
        return "bakje"

def get_topping():
    return validate_input(data.topping_message, ["A", "B", "C", "D"])

def validate_scoops():
    while True:
        try:
            scoops = int(input(data.scoops_message))
            if 1 <= scoops <= 8:
                return scoops
            else:
                print("We kunnen minimaal 1 en maximaal 8 bolletjes per bestelling accepteren.")
        except ValueError:
            print("Ongeldige invoer. Voer a.u.b. een getal in.")

def validate_liters():
    while True:
        try:
            liters = int(input("Hoeveel liter wilt u bestellen? "))
            if liters > 0:
                return liters
            else:
                print("We kunnen minimaal 1 liter per bestelling accepteren.")
        except ValueError:
            print("Ongeldige invoer. Voer a.u.b. een getal in.")

def validate_flavors(num_scoops):
    flavors = []
    for i in range(1, num_scoops + 1):
        while True:
            flavor = input(f"Welke smaak wilt u voor bolletje nummer {i}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ").strip().upper()
            if flavor in ['A', 'C', 'M', 'V']:
                if flavor == 'A':
                    flavors.append('aardbei')
                elif flavor == 'C':
                    flavors.append('chocolade')
                elif flavor == 'M':
                    flavors.append('munt')
                elif flavor == 'V':
                    flavors.append('vanille')
                break
            else:
                print("Sorry dat is geen optie die we aanbieden....")
    return flavors

def validate_liter_flavors(num_liters):
    flavors = {}
    for i in range(1, num_liters + 1):
        while True:
            flavor = input(f"Welke smaak wilt u voor liter nummer {i}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ").strip().upper()
            if flavor in ['A', 'C', 'M', 'V']:
                if flavor == 'A':
                    flavors['aardbei'] = flavors.get('aardbei', 0) + 1
                elif flavor == 'C':
                    flavors['chocolade'] = flavors.get('chocolade', 0) + 1
                elif flavor == 'M':
                    flavors['munt'] = flavors.get('munt', 0) + 1
                elif flavor == 'V':
                    flavors['vanille'] = flavors.get('vanille', 0) + 1
                break
            else:
                print("Sorry dat is geen optie die we aanbieden....")
    return flavors

def ask_customer_type():
    return validate_input("Bent u 1) een particuliere klant of 2) een zakelijke klant? ", ["1", "2"])

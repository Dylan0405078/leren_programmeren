# flow.py
import functions
import data

functions.welcome_message()

order = []
customer_type = functions.ask_customer_type()

if customer_type == '2':  # Zakelijke klant
    while True:
        liters = functions.validate_liters()
        flavors = functions.validate_liter_flavors(liters)
        total_price = liters * data.LITER_PRICE
        order_item = {'liters': liters, 'flavors': flavors, 'total_price': total_price}
        
        order.append(order_item)

        more_order = functions.validate_input(data.confirmation_message, ['JA', 'NEE'])
        if more_order == 'NEE':
            break
else:  # Particuliere klant
    while True:
        scoops = functions.validate_scoops()
        flavors = functions.validate_flavors(scoops)
        cone_or_cup = functions.get_cone_or_cup(scoops)
        topping_choice = functions.get_topping()
        if topping_choice == 'A':
            topping = 'geen'
        elif topping_choice == 'B':
            topping = 'slagroom'
        elif topping_choice == 'C':
            topping = 'sprinkels'
        elif topping_choice == 'D':
            topping = 'caramel saus'

        order_item = {'scoops': scoops, 'type': cone_or_cup, 'flavors': flavors, 'topping': topping}
        
        order.append(order_item)

        more_order = functions.validate_input(data.confirmation_message, ['JA', 'NEE'])
        if more_order == 'NEE':
            break

functions.print_receipt(order, customer_type)

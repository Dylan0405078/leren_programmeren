import functions
import data



functions.welcome_message()
order = []
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

functions.print_receipt(order)


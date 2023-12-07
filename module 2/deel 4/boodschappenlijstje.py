#boodschappenlijstje
def add_item(item, quantity, shopping_list):
    item = item.lower()
    if item in shopping_list:
        additional_quantity = int(input("Hoeveel wil je toevoegen? "))
        shopping_list[item] += additional_quantity
    else:
        shopping_list[item] = quantity

def print_list(shopping_list):
    print("- [ Boodschappenlijst ] -")
    for item, quantity in shopping_list.items():
        print(f"{quantity} x {item.capitalize()}")
    print("------------------------------------------")

def main():
    shopping_list = {}
  
    while True:
        item = input("Wat wil je toevoegen aan de lijst? ")
        quantity = int(input("Hoeveel wil je toevoegen? "))
        add_item(item, quantity, shopping_list)

        more = input("Wil je nog meer items toevoegen aan de lijst? (ja/nee): ")
        if more.lower() != "ja":
            break

    print_list(shopping_list)

if __name__ == "__main__":
    main()

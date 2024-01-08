#boodschappenlijstje
def print_list(shopping_list):
    print("#boodschappenlijstje")
    for item, quantity in shopping_list.items():
        print(f"{quantity} x {item.capitalize()}")
    print("------------------------------------------")

shopping_list = {}

while True:
    item = input("Wat wil je toevoegen aan de lijst? ").lower()
    quantity = int(input("Hoeveel wil je toevoegen? "))

    if item in shopping_list:
        shopping_list[item] += quantity
    else:
        shopping_list[item] = quantity

    more = input("Wil je nog meer items toevoegen aan de lijst? (ja/nee): ")
    if more.lower() != "ja":
        print_list(shopping_list)
        break


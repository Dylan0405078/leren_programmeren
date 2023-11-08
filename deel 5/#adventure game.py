#adventure game
from termcolor import colored

# Function to display text in blue color
def display_text(text):
    print(colored(text, 'red'))

# Introduction
display_text ("-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-")
display_text("WELCOME TO THE GAME SMALL TOWN. THIS IS A SMALL ADVENTURE GAME WHERE YOU HAVE TO COMPLETE CHOICES TO CONTINUE WITH THE STORY. BUT BEWARE, SOME CHOICES MAY BE FATAL TO YOUR CHARACTER CALLED 'DAVE'.\n")
display_text ("-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-")
# Start of the game
hat_choice = input("Would you like to wear a hat? (yes/no)\n")
if hat_choice.lower() == 'yes':
    horse_choice = input("DAVE meets a horse named 'Henkie'. Do you want to take him on a trip to the desert? (yes/no)\n")
    if horse_choice.lower() == 'yes':
        desert_choice = input("DAVE encounters a horde of criminals in the desert. Do you want to flee? (yes/no)\n")
        if desert_choice.lower() == 'yes':
            sheriff_choice = input("Nice! DAVE has escaped from the criminals. Would you like to alert the sheriff? (yes/no)\n")
            if sheriff_choice.lower() == 'yes':
                display_text("DAVE alerted the sheriff. He goes to the place. Will you go with him or will you go your own way? (along/own way)\n")
                sheriff_trip = input()
                if sheriff_trip.lower() == 'along':
                    display_text("DAVE goes with the sheriff and you arrest the criminals. You will also be appointed as the sheriff's assistant.")
                elif sheriff_trip.lower() == 'own way':
                    display_text("That's a shame because the criminals are not arrested. Do you want to continue on the route you were on or do you want to go to the village? (passage/village)\n")
                    village_choice = input()
                    if village_choice.lower() == 'passage':
                        display_text("DAVE trots on his horse past the criminals and out of their sight. Do you want to continue or are you going back? (further/back)\n")
                        passage_choice = input()
                        if passage_choice.lower() == 'further':
                            display_text("You continue, only DAVE and Henkie dry out and die in the middle of the desert.")
                        elif passage_choice.lower() == 'back':
                            display_text("Because DAVE has returned, you died of dehydration right next to the village, and a funeral is being prepared for you!")
                    elif village_choice.lower() == 'village':
                        display_text("DAVE arrives in the village. You see the criminals breaking into a salon. What do you do? (back and arrest/ignore)\n")
                        arrest_choice = input()
                        if arrest_choice.lower() == 'back and arrest':
                            display_text("DAVE has successfully arrested the criminals. DAVE has been chosen as the new sheriff of the village 'Small Town.'")
                        elif arrest_choice.lower() == 'ignore':
                            display_text("DAVE is arrested for complicity in burglary, and you end up in jail.")
                        else:
                            display_text("Invalid input. Game over.")
                    else:
                        display_text("Invalid input. Game over.")
                else:
                    display_text("Invalid input. Game over.")
            elif sheriff_choice.lower() == 'no':
                display_text("DAVE faces his fate and dies in front of the criminals.")
            else:
                display_text("Invalid input. Game over.")
        elif desert_choice.lower() == 'no':
            display_text("DAVE faces his fate and dies in front of the criminals.")
        else:
            display_text("Invalid input. Game over.")
    elif horse_choice.lower() == 'no':
        display_text("DAVE encounters a horde of criminals in the desert. Do you want to flee? (yes/no)\n")
        desert_choice = input()
        if desert_choice.lower() == 'yes':
            display_text("DAVE tried to flee, but because you don't have a horse, DAVE was shot dead by the criminals.")
        elif desert_choice.lower() == 'no':
            display_text("DAVE faces his fate and dies in front of the criminals.")
        else:
            display_text("Invalid input. Game over.")
    else:
        display_text("Invalid input. Game over.")
else:
    display_text("DAVE decides not to wear a hat and continues with the story.")
    horse_choice = input("DAVE meets a horse named 'Henkie'. Do you want to take him on a trip to the desert? (yes/no)\n")
    if horse_choice.lower() == 'yes':
        desert_choice = input("DAVE encounters a horde of criminals in the desert. Do you want to flee? (yes/no)\n")
        if desert_choice.lower() == 'yes':
            sheriff_choice = input("Nice! DAVE has escaped from the criminals. Would you like to alert the sheriff? (yes/no)\n")
            if sheriff_choice.lower() == 'yes':
                display_text("DAVE alerted the sheriff. He goes to the place. Will you go with him or will you go your own way? (along/own way)\n")
                sheriff_trip = input()
                if sheriff_trip.lower() == 'along':
                    display_text("DAVE goes with the sheriff and you arrest the criminals. You will also be appointed as the sheriff's assistant.")
                elif sheriff_trip.lower() == 'own way':
                    display_text("That's a shame because the criminals are not arrested. Do you want to continue on the route you were on or do you want to go to the village? (passage/village)\n")
                    village_choice = input()
                    if village_choice.lower() == 'passage':
                        display_text("DAVE trots on his horse past the criminals and out of their sight. Do you want to continue or are you going back? (further/back)\n")
                        passage_choice = input()
                        if passage_choice.lower() == 'further':
                            display_text("You continue, only DAVE and Henkie dry out and die in the middle of the desert.")
                        elif passage_choice.lower() == 'back':
                            display_text("Because DAVE has returned, you died of dehydration right next to the village, and a funeral is being prepared for you!")
                        else:
                            display_text("Invalid input. Game over.")
                    elif village_choice.lower() == 'village':
                        display_text("DAVE arrives in the village. You see the criminals breaking into a salon. What do you do? (back and arrest/ignore)\n")
                        arrest_choice = input()
                        if arrest_choice.lower() == 'back and arrest':
                            display_text("DAVE has successfully arrested the criminals. DAVE has been chosen as the new sheriff of the village 'Small Town.'")
                        elif arrest_choice.lower() == 'ignore':
                            display_text("DAVE is arrested for complicity in burglary, and you end up in jail.")
                        else:
                            display_text("Invalid input. Game over.")
                    else:
                        display_text("Invalid input. Game over.")
                else:
                    display_text("Invalid input. Game over.")
            elif sheriff_choice.lower() == 'no':
                display_text("DAVE faces his fate and dies in front of the criminals.")
            else:
                display_text("Invalid input. Game over.")
        elif desert_choice.lower() == 'no':
            display_text("DAVE faces his fate and dies in front of the criminals.")
        else:
            display_text("Invalid input. Game over.")
    elif horse_choice.lower() == 'no':
        display_text("DAVE encounters a horde of criminals in the desert. Do you want to flee? (yes/no)\n")
        desert_choice = input()
        if desert_choice.lower() == 'yes':
            display_text("DAVE tried to flee, but because you don't have a horse, DAVE was shot dead by the criminals.")
        elif desert_choice.lower() == 'no':
            display_text("DAVE faces his fate and dies in front of the criminals.")
        else:
            display_text("Invalid input. Game over.")
    else:
        display_text("Invalid input. Game over.")


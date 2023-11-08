import tkinter as tk
from tkinter import messagebox

# Create a function to display a message box
def show_message(message, title="Game Message", options=("1", "2")):
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    result = messagebox.askquestion(title, message, icon='info', type=messagebox.YESNO, default=messagebox.YES, parent=root)

    # Close the main window
    root.destroy()

    return result

# Function to handle the hat choice
def handle_hat_choice():
    choice = show_message("Would you like to wear a hat?", "Hat Choice")
    if choice == "yes":
        show_message("You chose to wear a hat.")
        handle_horse_choice()
    elif choice == "no":
        show_message("You chose not to wear a hat. Dave continues with the story.")
        handle_horse_choice()
    else:
        show_message("Invalid input. Game over.")

# Function to handle the horse choice
def handle_horse_choice():
    choice = show_message("Dave meets a horse named 'Henkie'. Do you want to take him on a trip to the desert?", "Horse Choice")
    if choice == "yes":
        handle_desert_choice()
    elif choice == "no":
        show_message("Dave encounters a horde of criminals in the desert. This part is in Small Town 2.")
        show_message("Dave faces his fate and dies in front of the criminals.")
    else:
        show_message("Invalid input. Game over.")

# Function to handle the desert choice
def handle_desert_choice():
    choice = show_message("Dave encounters a horde of criminals in the desert. Do you want to flee?", "Desert Choice")
    if choice == "yes":
        handle_sheriff_choice()
    elif choice == "no":
        show_message("Dave faces his fate and dies in front of the criminals.")
    else:
        show_message("Invalid input. Game over.")

# Function to handle the sheriff choice
def handle_sheriff_choice():
    choice = show_message("Nice! Dave has escaped from the criminals. Would you like to alert the sheriff?", "Sheriff Choice")
    if choice == "yes":
        choice = show_message("Dave alerted the sheriff. He goes to the place. Will you go with him or will you go your own way?", "Sheriff's Choice", ("1 (along)", "2 (own way)"))
        if choice == "1":
            show_message("Dave goes with the sheriff, and you arrest the criminals. You will also be appointed as the sheriff's assistant.")
        elif choice == "2":
            choice = show_message("That's a shame because the criminals are not arrested. Do you want to continue on the route you were on or do you want to go to the village?", "Continuation Choice", ("1 (passage)", "2 (village)"))
            if choice == "1":
                choice = show_message("Dave trots on his horse past the criminals and out of their sight. Do you want to continue or are you going back?", "Desert Passage", ("1 (further)", "2 (back)"))
                if choice == "1":
                    show_message("You continue, only Dave and Henkie dry out and die in the middle of the desert.")
                elif choice == "2":
                    show_message("Because Dave has returned, you died of dehydration right next to the village, and a funeral is being prepared for you!")
            elif choice == "2":
                choice = show_message("Dave arrives in the village. You see the criminals breaking into a salon. What do you do?", "Village Choice", ("1 (back and arrest)", "2 (ignore)"))
                if choice == "1":
                    show_message("Dave has successfully arrested the criminals. Dave has been chosen as the new sheriff of the village 'Small Town.'")
                elif choice == "2":
                    show_message("Dave is arrested for complicity in burglary, and you end up in jail.")
            else:
                show_message("Invalid input. Game over.")
        else:
            show_message("Invalid input. Game over.")
    elif choice == "no":
        show_message("Dave faces his fate and dies in front of the criminals.")
    else:
        show_message("Invalid input. Game over.")

# Start the game
handle_hat_choice()


# intro text
intro_text = [
    "-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-",
    "WELCOME TO THE GAME SMALL TOWN. THIS IS A SMALL ADVENTURE GAME WHERE YOU HAVE TO COMPLETE CHOICES TO CONTINUE WITH THE STORY. BUT BEWARE, SOME CHOICES MAY BE FATAL TO YOUR CHARACTER CALLED 'DAVE'.\n",
    "-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-"
]

# verhaallijn in dicts, Prompts, keuze keys en eind messages in overwinning/verlies.
story_steps = {
    "hat_choice": {
        "prompt": "Would you like to wear a hat? (yes/no)\n",
        "yes": "horse_choice",
        "no": "continue_without_hat"
    },
    "horse_choice": {
        "prompt": "DAVE meets a horse named 'Henkie'. Do you want to take him on a trip to the desert? (yes/no)\n",
        "yes": "desert_choice",
        "no": "encounter_criminals_no_horse"
    },
    "desert_choice": {
        "prompt": "DAVE encounters a horde of criminals in the desert. Do you want to flee? (yes/no)\n",
        "yes": "sheriff_choice",
        "no": "face_fate"
    },
    "sheriff_choice": {
        "prompt": "Nice! DAVE has escaped from the criminals. Would you like to alert the sheriff? (yes/no)\n",
        "yes": "sheriff_trip",
        "no": "face_fate"
    },
    "sheriff_trip": {
        "prompt": "DAVE alerted the sheriff. He goes to the place. Will you go with him or will you go your own way? (along/own way)\n",
        "along": "assist_sheriff",
        "own way": "route_choice"
    },
    "route_choice": {
        "prompt": "Do you want to continue on the route you were on or do you want to go to the village? (passage/village)\n",
        "passage": "continue_or_back",
        "village": "arrive_village"
    },
    "continue_or_back": {
        "prompt": "DAVE trots on his horse past the criminals and out of their sight. Do you want to continue or are you going back? (further/back)\n",
        "further": "die_in_desert",
        "back": "die_near_village"
    },
    "arrive_village": {
        "prompt": "DAVE arrives in the village. You see the criminals breaking into a salon. What do you do? (back and arrest/ignore)\n",
        "back and arrest": "arrest_criminals",
        "ignore": "arrested_for_complicity"
    },
    "continue_without_hat": {
        "prompt": "DAVE decides not to wear a hat and continues with the story.",
        "next": "horse_choice"
    },
    "encounter_criminals_no_horse": {
        "prompt": "DAVE encounters a horde of criminals in the desert. Do you want to flee? (yes/no)\n",
        "yes": "shot_dead",
        "no": "face_fate"
    },
    "assist_sheriff": {
        "message": "DAVE goes with the sheriff and you arrest the criminals. You will also be appointed as the sheriff's assistant."
    },
    "die_in_desert": {
        "message": "You continue, only DAVE and Henkie dry out and die in the middle of the desert."
    },
    "die_near_village": {
        "message": "Because DAVE has returned, you died of dehydration right next to the village, and a funeral is being prepared for you!"
    },
    "arrest_criminals": {
        "message": "DAVE has successfully arrested the criminals. DAVE has been chosen as the new sheriff of the village 'Small Town.'"
    },
    "arrested_for_complicity": {
        "message": "DAVE is arrested for complicity in burglary, and you end up in jail."
    },
    "shot_dead": {
        "message": "DAVE tried to flee, but because you don't have a horse, DAVE was shot dead by the criminals."
    },
    "face_fate": {
        "message": "DAVE faces his fate and dies in front of the criminals."
    }
}

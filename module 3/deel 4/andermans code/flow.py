from functions import display_text, get_input, play_game
from data import intro_text, story_steps

#opening laten zien
for line in intro_text:
    display_text(line)

# Game loop
play_game("hat_choice")

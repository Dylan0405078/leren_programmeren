from termcolor import colored
from data import intro_text, story_steps

# Function to display text in red color
def display_text(text):
    print(colored(text, 'red'))

# functie om een geldig antwoord te krijgen.
def get_input(prompt, valid_options):
    while True:
        choice = input(prompt).lower()
        if choice in valid_options:
            return choice
        display_text("Invalid input. Please try again.")
        
# runt de game en zorgt ervoor dat er gecontroleerd word op vragen, eindes en toont de prompts
def play_game(step):
    while step:
        if "prompt" in story_steps[step]:
            choice = get_input(story_steps[step]["prompt"], story_steps[step].keys() - {"prompt", "next"})
            step = story_steps[step][choice]
        elif "message" in story_steps[step]:
            display_text(story_steps[step]["message"])
            break
        elif "next" in story_steps[step]:
            step = story_steps[step]["next"]
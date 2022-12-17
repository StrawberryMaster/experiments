import random
from typing import Dict

def play_round(choices: Dict[str, str]):
    # Display the options to the user
    print("Enter 'r' for rock, 'p' for paper, or 's' for scissors")
    
    # Get the user's choice
    choice = input("Your choice: ")
    
    # Validate the user's choice
    if choice not in choices:
        print("Invalid choice")
        return
    
    # Generate the computer's choice
    computer_choice = random.choice(list(choices.keys()))
    
    # Determine the winner of the round
    if choice == computer_choice:
        print("Tie! You both chose", choice)
    elif choices[choice] == computer_choice:
        print("You win! Your", choice, "beats the computer's", computer_choice)
    else:
        print("Computer wins! Your", choice, "loses to the computer's", computer_choice)

# Map the choices to their respective wins/losses
choices = {'r': 's', 'p': 'r', 's': 'p'}

# Play a series of rounds until the user decides to stop
while True:
    play_round(choices)
    if input("Play again? (y/n) ") != 'y':
        break

# We define a function called play_round() that takes a dict of
# choices as an argument and plays a single round of the game.
# The dict maps each choice to the choice that it beats.
#
# We then prompt the user to enter their choice of 'rock',
# 'paper', or 'scissors', and then generate a random choice for
# the computer using the random module's choice() function and the dict keys.
#
# We then determines the winner of the round based on the rules of
# the game and the dict of choices, and print out the result along
# with the choices made by the user and the computer.
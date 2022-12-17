import random
from collections import Counter

def play_game():
    # Set up the game
    colors = ['red', 'yellow', 'green', 'blue']
    code = [random.choice(colors) for _ in range(4)]
    print("Code:", code)  # Debugging line
    
    # Play the game
    for i in range(10):
        # Get the user's guess
        guess = input("Enter your guess (4 colors): ").lower().split()
        
        # Validate the user's guess
        if len(guess) != 4:
            print("Invalid guess")
            continue
        for color in guess:
            if color not in colors:
                print("Invalid guess")
                break
        else:
            # Check the user's guess against the code
            code_count = Counter(code)
            guess_count = Counter(guess)
            correct_colors = sum((guess_count & code_count).values())
            correct_positions = sum(g == c for g, c in zip(guess, code))
            print("Correct colors:", correct_colors - correct_positions)
            print("Correct positions:", correct_positions)
            if correct_positions == 4:
                print("You won!")
                return
    
    # The user didn't guess the code in time
    print("You lost :( The code was", code)

# Play a series of games until the user decides to stop
while True:
    play_game()
    if input("Play again? (y/n) ") != 'y':
        break

# We are going to play the game of Mastermind. In this game, we have
# a code made up of four colors chosen from a list of four possible
# colors: red, yellow, green, and blue.
#
# To start the game, we randomly select four colors from the list of
# possible colors to be the code for this round of the game. We then
# enter a loop where the user has ten chances to guess the code.
# On each iteration of the loop, we ask the user to enter their guess,
# which is also a list of four colors.
#
# Before we check the user's guess against the code, we first validate
# the guess to make sure it is a valid input. We do this by checking that
# the user entered four colors and that all of the colors are valid choices.
# If the guess is not valid, we print an error message and skip the rest of
# the loop iteration.
#
# If the guess is valid, we compare it to the code. We use two different measures
# to evaluate the guess: the number of correct colors and the number of correct
# positions. To find the number of correct colors, we create two counters, one for
# the code and one for the guess, and then use the "&" operator to find the intersection
# of the two counters. The size of this intersection tells us how many colors are shared
# between the code and the guess. To find the number of correct positions, we use a
# list comprehension to compare the elements of the code and the guess pairwise and
# count the number of times they are equal.
#
# Finally, we check if the user has won by checking if the number of correct
# positions is equal to four. If it is, we print a winning message and exit
# the game. If the user runs out of chances before guessing the code correctly,
# we print a losing message and reveal the code to the user.
#
# After the game is over, we ask the user if they want to play again. If they do,
# we start a new game; if they don't, we exit the loop and the program terminates.
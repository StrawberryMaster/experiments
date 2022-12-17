import random

def play_game():
    # Set up the game
    words = ['cat', 'dog', 'bird', 'mouse']
    word = random.choice(words)
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()
    lives = 6
    
    # Play the game
    while len(word_letters) > 0 and lives > 0:
        # Print out the current game state
        print("You have", lives, "lives left")
        print("Used letters:", ' '.join(used_letters))
        print("Current word:", ' '.join([letter if letter in used_letters else '_' for letter in word]))
        
        # Get the user's next guess
        letter = input("Enter a letter: ").lower()
        
        # Validate the user's guess
        if letter in alphabet - used_letters:
            used_letters.add(letter)
            if letter in word_letters:
                word_letters.remove(letter)
            else:
                lives -= 1
        elif letter in used_letters:
            print("You have already used that letter")
        else:
            print("Invalid letter")
    
    # Print out the result of the game
    if lives == 0:
        print("You lost :( The word was", word)
    else:
        print("You won! The word was", word)

# Play a series of games until the user decides to stop
while True:
    play_game()
    if input("Play again? (y/n) ") != 'y':
        break

# We start by setting up the game by selecting a random word
# from a list of words and initializing some variables to track
# the state of the game. The list of words can be modified to
# change the difficulty of the game.
#
# Next, we enter a while loop that continues to play rounds of the
# game until we either correctly guess the word or run out of lives.
# Each round of the game consists of the following steps:
#
# 1. We print out the current game state, including the number of lives
# remaining, the letters that have been used, and the current state of the
# word (with correctly guessed letters revealed and all other letters
# replaced with underscores).
# 2. We prompt the user to enter their next guess.
# 3. We validate the user's guess and update the game state accordingly.
# If the guess is invalid, we print an error message. If the guess is a
# new letter that is in the word, we remove the letter from the set of
# letters that remain to be guessed. If the guess is a new letter that
# is not in the word, we reduce the number of lives remaining.
#
# After the while loop completes, we print out the result of the game.
# Finally, we enter another while loop that continues to play games
# of Hangman until the user decides to stop. The user can choose to
# stop by entering 'n' when prompted to play again.
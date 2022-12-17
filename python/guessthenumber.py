import random

def play_game():
  # Generate a random number between 1 and 100
  secret_number = random.randint(1, 100)

  # Ask the user to guess the number
  while True:
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
      print("You guessed correctly! The number was", secret_number)
      break
    elif guess < secret_number:
      print("Your guess is too low")
    else:
      print("Your guess is too high")

# Play the game until the user decides to stop
while True:
  play_game()
  if input("Play again? (y/n) ") != 'y':
    break

# A more sophisticated version of secretnumber.py.
# 
# In this game, we generate a random number between 1 and 100 
# and ask the user to guess it. We keep asking the user to enter
# their guess until they correctly guess the number. After each guess,
# we give the user feedback on whether their guess was too low, too high,
# or correct. Once the user has correctly guessed the number, we print a
# winning message and exit the game.
#
# After the game is over, we ask the user if they want to play again.
# If they do, we start a new game; if they don't, we exit the loop
# and the program terminates.
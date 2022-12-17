import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

while True:
    # Get a guess from the user
    guess = int(input("Enter a number between 1 and 10: "))

    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations, you guessed the correct number!")
        break
    else:
        print("Sorry, that was incorrect. Please try again.")

# In this example, we generates a random number between 1 and 10,
# and then ask the user to guess the number. If the user guesses
# correctly, we print a congratulatory message and exit; otherwise,
# we prompt the user to try again until they get the correct answer.
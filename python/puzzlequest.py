def game():
    level = 1
    puzzles_solved = 0

    # define the puzzles
    puzzles = {
        1: {
            1: {
                "prompt": "What is 1 + 1?",
                "answer": "2",
                "solved": False
            },
            2: {
                "prompt": "What is the capital of France?",
                "answer": "Paris",
                "solved": False
            },
            3: {
                "prompt": "What is the square root of 9?",
                "answer": "3",
                "solved": False
            }
        },
        2: {
            1: {
                "prompt": "What is the opposite of hot?",
                "answer": "cold",
                "solved": False
            },
            2: {
                "prompt": "What is the third planet from the sun?",
                "answer": "Earth",
                "solved": False
            },
            3: {
                "prompt": "What is the sum of 2 + 2?",
                "answer": "4",
                "solved": False
            }
        },
        3: {
            1: {
                "prompt": "What is the chemical symbol for hydrogen?",
                "answer": "H",
                "solved": False
            },
            2: {
                "prompt": "What is the capital of Japan?",
                "answer": "Tokyo",
                "solved": False
            },
            3: {
                "prompt": "What is the product of 3 x 3?",
                "answer": "9",
                "solved": False
            }
        }
    }

    while True:
        # display the available puzzles
        print(f"Level {level}:")
        for i, puzzle in puzzles[level].items():
            # check if puzzle has been solved
            if puzzle['solved']:
                # display puzzle as solved
                print(f"{i}. {puzzle['prompt']} (solved)")
            else:
                # display puzzle as not solved
                print(f"{i}. {puzzle['prompt']}")

        # get the player's puzzle choice
        try:
            puzzle_choice = int(
                input("\nEnter the number of the puzzle you want to solve: "))
        except ValueError:
            print("\nInvalid input. Please enter a valid puzzle number.")
            continue

        # display the puzzle and get the player's answer
        puzzle = puzzles[level][puzzle_choice]
        answer = input(puzzle['prompt'] + " ")

        # check if the player's answer is correct
        if answer.lower() == puzzle['answer'].lower():
            print("Correct!")
            # mark puzzle as solved
            puzzle['solved'] = True
            puzzles_solved += 1
            # check if the player has completed all the puzzles in the level
            if puzzles_solved == 3:
                print(f"Congratulations, you completed level {level}!")
                level += 1
                puzzles_solved = 0
                # check if the player has won the game
                if level > 3:
                    print("You solved all the puzzles! You win!")
                    break
        else:
            print("Incorrect. Please try again.")

game()

# In this game, the player must solve a series of increasingly difficult puzzles
# in order to progress. The game has three levels, and each level has three puzzles.
# The player must solve all three puzzles in a level to move on to the next level.
# The player wins the game by solving all three puzzles in all three levels.
# 
# When the game starts, the player is presented with a list of available puzzles
# and asked to choose one. The game displays the puzzle and prompts the player
# to enter their answer.  If the player's answer is correct, the game displays a
# message and moves on to the next puzzle. If the player's answer is incorrect,
# the game displays an error message and allows the player to try again.
#
# When the player completes all the puzzles in a level, they move on to the next level.
# If the player completes all the puzzles in all three levels, they win the game.
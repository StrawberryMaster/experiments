import random

# Constants
GRID_SIZE = 10
MINES = 10

# Generate the minefield
minefield = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
mines_remaining = MINES
while mines_remaining > 0:
    row = random.randint(0, GRID_SIZE - 1)
    col = random.randint(0, GRID_SIZE - 1)
    if minefield[row][col] != -1:
        minefield[row][col] = -1
        mines_remaining -= 1

# Calculate the numbers for each square
for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        if minefield[row][col] == -1:
            continue
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if r >= 0 and r < GRID_SIZE and c >= 0 and c < GRID_SIZE and minefield[
                        r][c] == -1:
                    minefield[row][col] += 1

# Initialize the game state
revealed = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
flags = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Game loop
while True:
    # Print the grid
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if flags[row][col]:
                print("F ", end="")
            elif revealed[row][col]:
                if minefield[row][col] == -1:
                    print("X ", end="")
                else:
                    print(f"{minefield[row][col]} ", end="")
            else:
                print("# ", end="")
        print()

    # Print the number of mines remaining
    mines_left = MINES
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if flags[row][col] and minefield[row][col] == -1:
                mines_left -= 1
    print(f"Mines remaining: {mines_left}")

    # Get the player's move
    move = input(
        "Enter your move (r row col to reveal, f row col to flag, c row col to chain reveal, q to quit): "
    )
    if move[0] == "r":
        row = int(move.split()[1])
        col = int(move.split()[2])
        if revealed[row][col]:
            print("You have already revealed that square.")
        elif flags[row][col]:
            print("You cannot reveal a flagged square.")
        elif minefield[row][col] == -1:
            print("You lost!")
            break
        else:
            revealed[row][col] = True
    elif move[0] == "f":
        row = int(move.split()[1])
        col = int(move.split()[2])
        if revealed[row][col]:
            print("You cannot flag a revealed square.")
        else:
            flags[row][col] = not flags[row][col]
    elif move[0] == "c":
        row = int(move.split()[1])
        col = int(move.split()[2])
        if not revealed[row][col]:
            print(
                "You cannot chain reveal a square that has not been revealed.")
            continue
        if minefield[row][col] == 0:
            queue = [(row, col)]
            while queue:
                r, c = queue.pop(0)
                if not revealed[r][c]:
                    revealed[r][c] = True
                    if minefield[r][c] == 0:
                        for rr in range(r - 1, r + 2):
                            for cc in range(c - 1, c + 2):
                                if rr >= 0 and rr < GRID_SIZE and cc >= 0 and cc < GRID_SIZE and not revealed[
                                        rr][cc]:
                                    queue.append((rr, cc))
        else:
            print("You can only chain reveal squares with value 0.")
    elif move[0] == "q":
        print("Thanks for playing!")
        break
    else:
        print("Invalid move.")

    # Check for win
    win = True
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if minefield[row][col] != -1 and not revealed[row][col]:
                win = False
                break
        if not win:
            break
    if win:
        print("You won!")
        break
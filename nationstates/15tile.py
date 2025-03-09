# Like kakuro.py, this was also made for NationStates' puzzles.
# This time, it's for the 15-tile puzzle. Here, you input a 4x4 grid
# with letters A-H and a blank tile represented by a period. The program
# will determine which letter is missing (aka the blank title/dot) tile in
# the solved puzzle) and then solve the puzzle.
# Honestly, it's better than the Kakuro one - at least in terms of, erm,
# the things I tinkered with.
# @author: StrawberryMaster

import heapq

# For our compact encoding we use 4 bits per tile.
# Letters A–H become 0–7, and we use 15 to represent the blank.
LETTER_TO_NUM = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
                 'E': 4, 'F': 5, 'G': 6, 'H': 7, '.': 15}
NUM_TO_LETTER = {v: k for k, v in LETTER_TO_NUM.items() if v != 15}
BLANK = 15

# Directions: each move is (name, (di, dj))
MOVES = {
    "up":    (-1,  0),
    "down":  ( 1,  0),
    "left":  ( 0, -1),
    "right": ( 0,  1)
}

def encode_board(board):
    """
    Given a 2D board (list of 4 lists of 4 ints), pack it into a 64-bit integer.
    Each cell uses 4 bits; cell 0 occupies bits 0–3, cell 1 uses bits 4–7, etc.
    """
    state = 0
    for i in range(4):
        for j in range(4):
            index = i * 4 + j
            # ensure value is only 4 bits
            state |= (board[i][j] & 0xF) << (index * 4)
    return state

def decode_state(state):
    """
    Unpack a 64-bit integer state into a tuple of 16 numbers.
    """
    return tuple((state >> (i * 4)) & 0xF for i in range(16))

def get_tile(state, index):
    """Return the tile at the given index (0..15) from the compact state."""
    return (state >> (index * 4)) & 0xF

def set_tile(state, index, value):
    """Set the tile at the given index in the compact state to value."""
    mask = 0xF << (index * 4)
    state &= ~mask
    state |= (value & 0xF) << (index * 4)
    return state

def swap_tiles(state, i, j):
    """
    Swap the tiles at indices i and j in the compact state.
    """
    ti = get_tile(state, i)
    tj = get_tile(state, j)
    state = set_tile(state, i, tj)
    state = set_tile(state, j, ti)
    return state

def create_goal_board(goal_blank):
    """
    Create the goal board as a 2D list (4x4) like the pattern below:
      A A B B
      C C D D
      E E F F
      G G H H
    Then remove the tile at position goal_blank by setting it to BLANK.
    """
    pattern = [
        [0, 0, 1, 1],  # A A B B
        [2, 2, 3, 3],  # C C D D
        [4, 4, 5, 5],  # E E F F
        [6, 6, 7, 7]   # G G H H
    ]
    flat = []
    for i in range(4):
        for j in range(4):
            flat.append(pattern[i][j])
    flat[goal_blank] = BLANK
    # convert flat list to a 2D board
    board = [flat[i*4:(i+1)*4] for i in range(4)]
    return board

def compute_goal_positions(goal_state_tuple):
    """
    For each letter tile (0 to 7), record the list of positions (row, col)
    in the goal state (tuple of 16) where that tile should be.
    Also return the (row, col) of the blank.
    """
    positions = {tile: [] for tile in range(8)}
    goal_blank_pos = None
    for index, value in enumerate(goal_state_tuple):
        pos = (index // 4, index % 4)
        if value == BLANK:
            goal_blank_pos = pos
        else:
            positions[value].append(pos)
    return positions, goal_blank_pos

def manhattan(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])

def compute_heuristic(state_tuple, goal_positions, goal_blank_pos):
    """
    Compute total Manhattan distance for each letter tile (optimally assigned)
    plus the Manhattan distance for the blank. Fun, right?
    """
    cost = 0
    for tile in range(8):
        curr_positions = [(i, j) for i in range(4) for j in range(4) 
                          if state_tuple[i*4+j] == tile]
        targets = goal_positions[tile]
        if not curr_positions:
            continue
        elif len(curr_positions) == 1:
            cost += min(manhattan(curr_positions[0], t) for t in targets)
        elif len(curr_positions) == 2:
            d1 = manhattan(curr_positions[0], targets[0]) + manhattan(curr_positions[1], targets[1])
            d2 = manhattan(curr_positions[0], targets[1]) + manhattan(curr_positions[1], targets[0])
            cost += min(d1, d2)
    # blank's distance
    blank_index = state_tuple.index(BLANK)
    blank_pos = (blank_index // 4, blank_index % 4)
    cost += manhattan(blank_pos, goal_blank_pos)
    return cost

def linear_conflict(state_tuple, goal_positions):
    conflict = 0
    # check rows
    for i in range(4):
        row = [state_tuple[i*4+j] for j in range(4)]
        for j in range(4):
            for k in range(j+1, 4):
                t1, t2 = row[j], row[k]
                if t1 == BLANK or t2 == BLANK:
                    continue
                # only consider tiles that belong in this row
                targets1 = [pos for pos in goal_positions[t1] if pos[0] == i]
                targets2 = [pos for pos in goal_positions[t2] if pos[0] == i]
                if targets1 and targets2 and targets1[0][1] > targets2[0][1]:
                    conflict += 2
    # check columns
    for j in range(4):
        col = [state_tuple[i*4+j] for i in range(4)]
        for i in range(4):
            for k in range(i+1, 4):
                t1, t2 = col[i], col[k]
                if t1 == BLANK or t2 == BLANK:
                    continue
                targets1 = [pos for pos in goal_positions[t1] if pos[1] == j]
                targets2 = [pos for pos in goal_positions[t2] if pos[1] == j]
                if targets1 and targets2 and targets1[0][0] > targets2[0][0]:
                    conflict += 2
    return conflict

def compute_heuristic_with_conflict(state_tuple, goal_positions, goal_blank_pos):
    return compute_heuristic(state_tuple, goal_positions, goal_blank_pos) + linear_conflict(state_tuple, goal_positions)

def get_neighbors_compact(state):
    """
    Generate all possible neighbors of the current state.
    Each neighbor is a tuple (new_state, move).
    """
    # find the blank index
    for i in range(16):
        if get_tile(state, i) == BLANK:
            blank_index = i
            break
    i, j = blank_index // 4, blank_index % 4
    for move, (di, dj) in MOVES.items():
        ni, nj = i + di, j + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            new_index = ni * 4 + nj
            new_state = swap_tiles(state, blank_index, new_index)
            yield (new_state, move)

def solve_puzzle_compact(initial_state, goal_state):
    """
    Solve the 15-tile puzzle using A* search with the Manhattan distance heuristic.
    The state is encoded as a 64-bit integer.
    """
    # decode goal state and compute goal positions
    goal_state_tuple = decode_state(goal_state)
    goal_positions, goal_blank_pos = compute_goal_positions(goal_state_tuple)
    
    # compute heuristic for initial state
    init_tuple = decode_state(initial_state)
    start_h = compute_heuristic_with_conflict(init_tuple, goal_positions, goal_blank_pos)
    
    frontier = [(start_h, 0, initial_state, [])]
    visited = {initial_state: 0}
    
    while frontier:
        f, g, current, path = heapq.heappop(frontier)
        if decode_state(current) == goal_state_tuple:
            return path
        for neighbor, move in get_neighbors_compact(current):
            new_cost = g + 1
            if neighbor not in visited or new_cost < visited[neighbor]:
                visited[neighbor] = new_cost
                neighbor_tuple = decode_state(neighbor)
                h = compute_heuristic_with_conflict(neighbor_tuple, goal_positions, goal_blank_pos)
                heapq.heappush(frontier, (new_cost + h, new_cost, neighbor, path + [move]))
    return None

def parse_board(input_str):
    """
    Parse a multi-line string board.
    Each line should have 4 tokens (letters A-H or '.' for blank).
    Returns a 2D list of ints.
    """
    board = []
    for line in input_str.strip().splitlines():
        tokens = line.strip().split()
        if len(tokens) != 4:
            raise ValueError("Each row must have exactly 4 tokens.")
        row = [LETTER_TO_NUM[token] for token in tokens]
        board.append(row)
    if len(board) != 4:
        raise ValueError("There must be exactly 4 rows.")
    return board

def determine_missing_letter(board):
    """
    In the solved puzzle each letter A–H appears twice.
    Return the letter that appears only once (ignoring blanks).
    """
    freq = {letter: 0 for letter in "ABCDEFGH"}
    for row in board:
        for tile in row:
            if tile != BLANK:
                freq[NUM_TO_LETTER[tile]] += 1
    missing = [letter for letter, count in freq.items() if count == 1]
    if len(missing) != 1:
        raise ValueError("Puzzle should have exactly one missing duplicate. Found: " + str(missing))
    return missing[0]

def print_board_from_state(state):
    """Decode the compact state and print it as a 4x4 board."""
    state_tuple = decode_state(state)
    for i in range(4):
        row = state_tuple[i*4:(i+1)*4]
        print(" ".join(NUM_TO_LETTER.get(tile, '.') if tile != BLANK else '.' for tile in row))
    print()

def main():
    print("Enter your puzzle (4 rows, 4 tokens per row).")
    print("Use letters A-H and '.' for the blank.")
    user_input = []
    for i in range(4):
        row = input(f"Row {i+1}: ")
        user_input.append(row)
    board_str = "\n".join(user_input)
    
    board = parse_board(board_str)
    initial_state = encode_board(board)
    
    missing_letter = determine_missing_letter(board)
    print("\nMissing letter (to be blank in solved puzzle):", missing_letter)
    
    # mapping: in the solved pattern "A A B B, C C D D, E E F F, G G H H",
    # we choose the second occurrence for the missing letter.
    GOAL_BLANK_POSITIONS = {
         'A': 1,
         'B': 3,
         'C': 5,
         'D': 7,
         'E': 9,
         'F': 11,
         'G': 13,
         'H': 15
    }
    goal_blank = GOAL_BLANK_POSITIONS[missing_letter]
    goal_board = create_goal_board(goal_blank)
    goal_state = encode_board(goal_board)
    
    print("\nInitial board:")
    print_board_from_state(initial_state)
    
    print("Goal board:")
    print_board_from_state(goal_state)
    
    print("Searching for a solution...")
    solution = solve_puzzle_compact(initial_state, goal_state)
    if solution is None:
        print("No solution found.")
    else:
        print("Solution ({} moves):".format(len(solution)))
        print(" -> ".join(solution))

if __name__ == "__main__":
    main()

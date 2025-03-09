# This was made to help me understand how to solve a Kakuro puzzle
# because I genuinely forgot. Sorry.
# Was especially useful when it came to helping me solve NationStates'
# very own simplified Kakuro puzzles.
# This may not be very optimized, but it works. I'm happy with it.
# But again, my apologies. Mea culpa, mea culpa, mea maxima culpa.
# @author: StrawberryMaster

import tkinter as tk
from tkinter import simpledialog
from itertools import combinations
import copy

def get_segments(grid):
    rows, cols = len(grid), len(grid[0])
    row_segments, col_segments = [], []
    
    # Horizontal (row) segments
    for i in range(1, rows):
        clue = grid[i][0]
        cells = []
        for j in range(1, cols):
            if grid[i][j] == " ":
                cells.append((i, j))
        if cells:
            row_segments.append({'clue': clue, 'cells': cells})
    
    # Vertical (column) segments
    for j in range(1, cols):
        clue = grid[0][j]
        cells = []
        for i in range(1, rows):
            if grid[i][j] == " ":
                cells.append((i, j))
        if cells:
            col_segments.append({'clue': clue, 'cells': cells})
    
    print("Row segments:", row_segments)
    print("Column segments:", col_segments)
    return row_segments, col_segments

def min_max_sum(used, remaining_cells):
    available = set(range(1, 10)) - used
    n = len(remaining_cells)
    if n == 0:
        return 0, 0
    sorted_avail = sorted(available)
    min_sum = sum(sorted_avail[:n])
    max_sum = sum(sorted_avail[-n:])
    return min_sum, max_sum

def solve_kakuro(grid):
    row_segments, col_segments = get_segments(grid)
    solution = [row.copy() for row in grid]
    empty_cells = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == " "]
    
    def is_valid(cell, num):
        i, j = cell
        # Check uniqueness in row and column
        row = [solution[i][col] for col in range(len(solution[i])) if solution[i][col] != " " and col != j]
        if num in row:
            return False
        col = [solution[row][j] for row in range(len(solution)) if solution[row][j] != " " and row != i]
        if num in col:
            return False
        
        # Check row segment constraints
        for seg in row_segments:
            if cell in seg['cells']:
                current_sum = num
                used = {num}
                remaining = []
                for (r, c) in seg['cells']:
                    if (r, c) == cell:
                        continue
                    val = solution[r][c]
                    if isinstance(val, int):
                        current_sum += val
                        if val in used:
                            return False
                        used.add(val)
                    else:
                        remaining.append((r, c))
                min_r, max_r = min_max_sum(used, remaining)
                if current_sum + min_r > seg['clue'] or current_sum + max_r < seg['clue']:
                    return False
        
        # Check column segment constraints
        for seg in col_segments:
            if cell in seg['cells']:
                current_sum = num
                used = {num}
                remaining = []
                for (r, c) in seg['cells']:
                    if (r, c) == cell:
                        continue
                    val = solution[r][c]
                    if isinstance(val, int):
                        current_sum += val
                        if val in used:
                            return False
                        used.add(val)
                    else:
                        remaining.append((r, c))
                min_r, max_r = min_max_sum(used, remaining)
                if current_sum + min_r > seg['clue'] or current_sum + max_r < seg['clue']:
                    return False
        
        return True
    
    from itertools import permutations
    def backtrack(index):
        if index == len(empty_cells):
            return True
        i, j = empty_cells[index]
        for num in range(1, 10):
            if is_valid((i, j), num):
                solution[i][j] = num
                if backtrack(index + 1):
                    return True
                solution[i][j] = " "
        return False
    
    backtrack(0)
    return solution

class KakuroGUI:
    def __init__(self, size=5):
        self.root = tk.Tk()
        self.size = size
        self.grid = [["B" if i == 0 or j == 0 else " " 
                      for j in range(size)] for i in range(size)]
        self.cells = {}
        self.setup_gui()
        
    def setup_gui(self):
        self.root.title("Kakuro Puzzle Solver")
        for i in range(self.size):
            for j in range(self.size):
                cell = tk.Button(self.root, width=5, height=2,
                               command=lambda r=i, c=j: self.cell_click(r, c))
                cell.grid(row=i, column=j)
                self.cells[(i, j)] = cell
                self.update_cell_display(i, j)
        
        button_frame = tk.Frame(self.root)
        button_frame.grid(row=self.size, column=0, columnspan=self.size)
        
        solve_button = tk.Button(button_frame, text="Solve", command=self.solve_puzzle)
        solve_button.pack(side=tk.LEFT, padx=5)
        
        reset_button = tk.Button(button_frame, text="Reset", command=self.reset_puzzle)
        reset_button.pack(side=tk.LEFT, padx=5)
        
    def reset_puzzle(self):
        self.grid = [["B" if i == 0 or j == 0 else " " 
                      for j in range(self.size)] for i in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                self.update_cell_display(i, j)
        
    def cell_click(self, i, j):
        current = self.grid[i][j]
        if current == " ":
            self.grid[i][j] = "B"
        elif current == "B":
            clue = simpledialog.askinteger("Input", 
                "Enter the clue for this cell (cancel if no clue):",
                parent=self.root, 
                minvalue=1, 
                maxvalue=45)
            self.grid[i][j] = clue if clue is not None else " "
        else:
            self.grid[i][j] = " "
        self.update_cell_display(i, j)
        
    def update_cell_display(self, i, j):
        cell = self.cells[(i, j)]
        value = self.grid[i][j]
        cell.config(text=str(value) if value != " " else "",
                   bg="black" if value == "B" else "white",
                   fg="white" if value == "B" else "black")
        
    def solve_puzzle(self):
        solution = solve_kakuro(self.grid)
        if solution:
            self.display_solution(solution)
        else:
            tk.messagebox.showerror("Error", "Unable to solve the puzzle. Have you entered all the clues?")
            
    def display_solution(self, solution):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == " ":
                    self.cells[(i, j)].config(text=str(solution[i][j]))
                    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = KakuroGUI(5)
    app.run()
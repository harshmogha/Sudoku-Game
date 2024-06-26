import tkinter as tk
from tkinter import messagebox
import random

class SudokuGenerator:
    def __init__(self, difficulty="easy"):
        self.grid = [[0] * 9 for _ in range(9)]
        self.solution = [[0] * 9 for _ in range(9)]
        self.difficulty = difficulty
        self.fill_grid()
        self.solution = [row[:] for row in self.grid]
        self.remove_numbers()

    def is_valid(self, num, row, col):
        if num in self.grid[row]:
            return False
        if num in [self.grid[i][col] for i in range(9)]:
            return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False
        return True

    def fill_grid(self):
        numbers = list(range(1, 10))
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    random.shuffle(numbers)
                    for num in numbers:
                        if self.is_valid(num, i, j):
                            self.grid[i][j] = num
                            if not any(0 in row for row in self.grid) or self.fill_grid():
                                return True
                            self.grid[i][j] = 0
                    return False
        return True

    def remove_numbers(self):
        if self.difficulty == "easy":
            num_remove = 30
        elif self.difficulty == "medium":
            num_remove = 40
        else:
            num_remove = 50

        while num_remove > 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            while self.grid[row][col] == 0:
                row, col = random.randint(0, 8), random.randint(0, 8)
            self.grid[row][col] = 0
            num_remove -= 1

class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid

    def is_valid(self, num, row, col):
        if num in self.grid[row]:
            return False
        if num in [self.grid[i][col] for i in range(9)]:
            return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False
        return True

    def solve(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    for num in range(1, 10):
                        if self.is_valid(num, i, j):
                            self.grid[i][j] = num
                            if not any(0 in row for row in self.grid) or self.solve():
                                return True
                            self.grid[i][j] = 0
                    return False
        return True

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Generator and Solver")
        self.root.configure(bg='#f0f0f0')  # Change the background color of the main window

        self.difficulty = tk.StringVar(value="easy")

        self.difficulty_label = tk.Label(self.root, text="Select Difficulty:", bg='#f0f0f0', font=('Helvetica', 12))
        self.difficulty_label.grid(row=0, column=0)

        self.easy_radio = tk.Radiobutton(self.root, text="Easy", variable=self.difficulty, value="easy", bg='#f0f0f0', font=('Helvetica', 12))
        self.easy_radio.grid(row=1, column=0)

        self.medium_radio = tk.Radiobutton(self.root, text="Medium", variable=self.difficulty, value="medium", bg='#f0f0f0', font=('Helvetica', 12))
        self.medium_radio.grid(row=2, column=0)

        self.hard_radio = tk.Radiobutton(self.root, text="Hard", variable=self.difficulty, value="hard", bg='#f0f0f0', font=('Helvetica', 12))
        self.hard_radio.grid(row=3, column=0)

        self.generate_button = tk.Button(self.root, text="Generate Sudoku", command=self.generate_sudoku, bg='#87CEFA', font=('Helvetica', 12))
        self.generate_button.grid(row=4, column=0)

        self.solve_button = tk.Button(self.root, text="Solve Sudoku", command=self.solve_sudoku, bg='#90EE90', font=('Helvetica', 12))
        self.solve_button.grid(row=5, column=0)

        self.validate_button = tk.Button(self.root, text="Validate Sudoku", command=self.validate_sudoku, bg='#FFD700', font=('Helvetica', 12))
        self.validate_button.grid(row=6, column=0)

        self.hint_button = tk.Button(self.root, text="Hint", command=self.provide_hint, bg='#FF69B4', font=('Helvetica', 12))
        self.hint_button.grid(row=7, column=0)
        self.hint_button.grid_remove()

        self.selected_cell = None
        self.create_sudoku_grid()

    def generate_sudoku(self):
        self.sudoku_generator = SudokuGenerator(difficulty=self.difficulty.get())
        self.sudoku_solver = SudokuSolver(self.sudoku_generator.grid)
        self.update_sudoku_grid(self.sudoku_generator.grid)
        self.hint_button.grid()

    def solve_sudoku(self):
        user_grid = self.get_user_grid()
        if not any(0 in row for row in user_grid):
            messagebox.showinfo("Sudoku Solved", "Sudoku puzzle already solved!")
        else:
            self.sudoku_solver = SudokuSolver(user_grid)
            if self.sudoku_solver.solve():
                self.update_sudoku_grid(user_grid)
                messagebox.showinfo("Sudoku Solved", "Sudoku puzzle solved successfully!")
            else:
                messagebox.showerror("Sudoku Solve Error", "Could not solve Sudoku puzzle!")

    def validate_sudoku(self):
        if hasattr(self, 'sudoku_generator'):
            user_grid = self.get_user_grid()
            if user_grid == self.sudoku_generator.solution:
                messagebox.showinfo("Sudoku Validation", "Congratulations! The Sudoku puzzle is correct!")
            else:
                messagebox.showerror("Sudoku Validation", "Some entries are incorrect/left. Please try again.")
        else:
            messagebox.showerror("Error", "Generate a Sudoku puzzle first!")

    def provide_hint(self):
        if self.selected_cell:
            i, j = self.selected_cell
            if self.entries[i * 9 + j].get() == "":
                number = self.sudoku_generator.solution[i][j]
                operation, result = self.generate_math_operation(number)
                self.show_math_operation_popup(operation, result, i, j)

    def generate_math_operation(self, number):
        op = random.choice(['+', '-', '*'])
        if op == '+':
            a = random.randint(1, number-1)
            b = number - a
            operation = f"{a} + {b}"
        elif op == '-':
            a = random.randint(number, number + 10)
            b = a - number
            operation = f"{a} - {b}"
        else:
            factors = [i for i in range(1, number + 1) if number % i == 0]
            a = random.choice(factors)
            b = number // a
            operation = f"{a} * {b}"
        return operation, number

    def show_math_operation_popup(self, operation, result, row, col):
        def check_answer():
            try:
                user_answer = int(answer_entry.get())
                if user_answer == result:
                    self.entries[row * 9 + col].delete(0, tk.END)
                    self.entries[row * 9 + col].insert(0, result)
                    popup.destroy()
                else:
                    messagebox.showerror("Incorrect Answer", "The answer is incorrect. Try again.")
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid integer.")

        popup = tk.Toplevel(self.root)
        popup.title("Solve the Operation")

        question_label = tk.Label(popup, text=f"Solve: {operation}", font=('Helvetica', 12))
        question_label.pack()

        answer_entry = tk.Entry(popup, font=('Helvetica', 12))
        answer_entry.pack()

        submit_button = tk.Button(popup, text="Submit", command=check_answer, font=('Helvetica', 12))
        submit_button.pack()

    def create_sudoku_grid(self):
        self.entries = []
        subgrid_colors = ["#fffacd", "#ffebcd", "#e0ffff", "#f0e68c", "#f5deb3", "#e6e6fa", "#d8bfd8", "#dda0dd", "#ffe4e1"]
        for i in range(9):
            for j in range(9):
                subgrid_index = (i // 3) * 3 + (j // 3)
                entry = tk.Entry(self.root, width=5, justify="center", bg=subgrid_colors[subgrid_index], font=('Helvetica', 16))
                entry.grid(row=i + 8, column=j + 1, ipadx=5, ipady=5)
                entry.bind("<FocusIn>", lambda event, i=i, j=j: self.set_selected_cell(i, j))
                self.entries.append(entry)

    def set_selected_cell(self, row, col):
        self.selected_cell = (row, col)

    def update_sudoku_grid(self, grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] != 0:
                    self.entries[i * 9 + j].delete(0, tk.END)
                    self.entries[i * 9 + j].insert(0, grid[i][j])
                else:
                    self.entries[i * 9 + j].delete(0, tk.END)

    def get_user_grid(self):
        user_grid = [[0] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                entry_value = self.entries[i * 9 + j].get()
                if entry_value.isdigit():
                    user_grid[i][j] = int(entry_value)
        return user_grid

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()

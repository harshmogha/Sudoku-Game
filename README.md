# Sudoku Generator and Solver

This project is a graphical Sudoku game implemented using Python and Tkinter. It allows users to generate Sudoku puzzles of varying difficulty levels, solve them, validate their solutions, and even get hints through math operations. 

## Features

- **Generate Sudoku**: Generates a Sudoku puzzle with three difficulty levels: easy, medium, and hard.
- **Solve Sudoku**: Solves the current Sudoku puzzle.
- **Validate Sudoku**: Checks if the user's solution matches the generated solution.
- **Provide Hint**: Offers hints by presenting math operations to solve for the correct number in a selected cell.

## Installation

1. Ensure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org/).

2. Install the required packages. Tkinter is included with Python, but if it's not installed, you can install it using:
   ```sh
   pip install tk
   ```

3. Download or clone this repository.

## Usage

1. Run the script:
   ```sh
   python sudoku.py
   ```

2. The GUI will appear with options to select the difficulty level, generate a Sudoku puzzle, solve it, validate it, and get hints.

### GUI Overview

- **Select Difficulty**: Choose the difficulty level (Easy, Medium, Hard) for generating a Sudoku puzzle.
- **Generate Sudoku**: Click to generate a new Sudoku puzzle based on the selected difficulty.
- **Solve Sudoku**: Click to automatically solve the current Sudoku puzzle.
- **Validate Sudoku**: Click to validate your solution against the correct solution.
- **Hint**: Click to get a hint for the selected cell by solving a math operation.

## Code Structure

- **SudokuGenerator**: Class to generate a Sudoku puzzle and remove numbers based on difficulty.
- **SudokuSolver**: Class to solve a given Sudoku puzzle.
- **SudokuGUI**: Class to create and manage the Tkinter GUI, handling user interactions and integrating with the SudokuGenerator and SudokuSolver classes.

## How It Works

### Generating a Sudoku Puzzle
1. The `SudokuGenerator` class initializes a 9x9 grid.
2. The `fill_grid` method recursively fills the grid with numbers ensuring no duplicate numbers in rows, columns, or 3x3 subgrids.
3. The `remove_numbers` method removes a specified number of cells based on the difficulty level.

### Solving a Sudoku Puzzle
1. The `SudokuSolver` class takes a grid and solves it using backtracking.
2. The `solve` method tries numbers from 1 to 9 in empty cells, ensuring each number is valid.

### GUI Interaction
1. The `SudokuGUI` class creates the main window and widgets using Tkinter.
2. The user can generate a Sudoku puzzle, solve it, validate their solution, and get hints by interacting with the buttons.

## Contributions

Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

import random
from typing import List, Tuple
from solving_algorithms import is_valid
Board = List[List[int]]

def generate_full_sudoku() -> Board:
    """
    Generate a completely solved Sudoku board.

    Returns:
        A fully solved Sudoku board.
    """
    # Initialize an empty board
    board = [[0] * 9 for _ in range(9)]

    # Recursive backtracking function to fill the board
    def fill_board(row: int, col: int) -> bool:
        if row == 9:
            return True  # Sudoku is complete
        next_row, next_col = (row, col + 1) if col < 8 else (row + 1, 0)

        if board[row][col] != 0:
            return fill_board(next_row, next_col)

        numbers = list(range(1, 10))
        random.shuffle(numbers)

        for num in numbers:
            if is_valid(board, row, col, num):
                board[row][col] = num
                if fill_board(next_row, next_col):
                    return True
                board[row][col] = 0  # Backtrack
        return False

    fill_board(0, 0)
    return board


def remove_numbers(board: Board, difficulty: int = 40) -> Board:
    """
    Remove numbers from a solved Sudoku board to create a puzzle.

    Args:
        board: A fully solved Sudoku board.
        difficulty: Number of cells to remove (40 is typical for medium difficulty).

    Returns:
        A partially filled Sudoku board (a puzzle).
    """
    puzzle = [row.copy() for row in board]
    cells = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(cells)

    for _ in range(difficulty):
        row, col = cells.pop()
        puzzle[row][col] = 0

    return puzzle


def generate_sudoku_puzzle(difficulty: int = 40) -> Board:
    """
    Generate a Sudoku puzzle of specified difficulty.

    Args:
        difficulty: Number of cells to remove (40 is typical for medium difficulty).

    Returns:
        A Sudoku puzzle.
    """
    solved_board = generate_full_sudoku()
    return remove_numbers(solved_board, difficulty)

import time
from typing import List, Optional, Tuple

Board = List[List[int]]


def is_valid(board: Board, row: int, col: int, num: int) -> bool:
    """
    Check if placing a number is valid.

    Args:
        board: The current Sudoku board.
        row: Row index.
        col: Column index.
        num: Number to place.
    
    Returns:
        True if valid, False otherwise.
    """
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True


def print_board(board: Board, new_positions: Optional[List[Tuple[int, int]]] = None):
    """
    Helper function to print the Sudoku board with grid lines.
    New positions are highlighted in green.

    Args:
        board: The Sudoku board.
        new_positions: List of new positions to highlight in green.

    Returns:
        None
    """
    GREEN = "\033[92m"  # ANSI code for green text
    RESET = "\033[0m"  # ANSI code to reset text color

    # Default to empty list if None
    new_positions = new_positions or []

    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # Add a horizontal separator every 3 rows
        for j, cell in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")  # Add a vertical separator every 3 columns

            # Highlight new positions in green
            if (i, j) in new_positions and cell != 0:
                print(f"{GREEN}{cell}{RESET}", end=" ")
            else:
                print(" " if cell == 0 else cell, end=" ")
        print()  # New line after each row


def solve_bfs(board: Board, show_steps: bool = False) -> Optional[Board]:
    """
    Solve Sudoku using BFS with optional step display.

    Args:
        board: The Sudoku board to solve.
        show_steps: Whether to show each step of the solution.

    Returns:
        The solved Sudoku board if a solution is found, None otherwise.
    """
    # Initialize a queue for Breadth-First Search (BFS).
    # Each element in the queue is a tuple (board, row, col).
    # Start at the top-left corner of the board (0, 0).
    queue = [(board, 0, 0)]
    step_count = 0 

    # Loop until the queue is empty.
    while queue:
        # Dequeue the first element from the queue.
        current_board, row, col = queue.pop(0)

        # If we reach row 9, the puzzle is solved since we go row by row.
        if row == 9:
            print()
            print(f"Total Cost: {step_count}")  # Optionally display the total steps or cost.
            return current_board  # Return the solved board.

        # Determine the next cell's row and column.
        # If we're not at the last column, move to the next column.
        # If we're at the last column, move to the first column of the next row.
        next_row, next_col = (row, col + 1) if col < 8 else (row + 1, 0)

        # If the current cell already has a number, skip it and continue to the next cell.
        if current_board[row][col] != 0:
            queue.append((current_board, next_row, next_col))
        else:
            # Try placing numbers 1 through 9 in the current empty cell.
            for num in range(1, 10):
                # Check if placing 'num' in the current cell is valid.
                if is_valid(current_board, row, col, num):
                    # Create a copy of the board to avoid modifying the original.
                    new_board = [r[:] for r in current_board]

                    # Place the number in the current cell.
                    new_board[row][col] = num

                    # Add the updated board to the queue to explore further.
                    queue.append((new_board, next_row, next_col))

                    # If step display is enabled, print the current step and board.
                    step_count += 1  # Increment the step counter.
                    if show_steps:
                        print(f"\nStep {step_count}:")
                        print_board(new_board, new_positions=[(row, col)])  # Highlight the added number.
                        time.sleep(0.5)  # Add a delay to visualize the step progression.

    # If the queue is exhausted and no solution is found, return None.
    return None


def solve_dfs(board: Board, show_steps: bool = False) -> Optional[Board]:
    """
    Solve Sudoku using DFS with optional step display.

    Args:
        board: The Sudoku board to solve.
        show_steps: Whether to show each step of the solution.

    Returns:
        The solved Sudoku board if a solution is found, None otherwise.
    """

    def dfs(board: Board, row: int, col: int) -> bool:
        nonlocal step_count  # Counter to track the number of steps

        # Base case: If we've processed all rows, the puzzle is solved.
        if row == 9:
            print()
            print(f"Total Cost: {step_count}")  # Print the total steps taken
            return True  # Puzzle solved

        # Move to the next column. If at the end of the row, move to the next row.
        next_row, next_col = (row, col + 1) if col < 8 else (row + 1, 0)

        # If the current cell already has a number (not 0), move to the next cell.
        if board[row][col] != 0:
            return dfs(board, next_row, next_col)

        # Try placing each number from 1 to 9 in the current empty cell.
        for num in range(1, 10):
            # Check if placing 'num' in the current cell is valid.
            if is_valid(board, row, col, num):
                # Place the number in the current cell.
                board[row][col] = num

                # Show the current step if enabled.
                step_count += 1  # Increment the step counter
                if show_steps:
                    print(f"\nStep {step_count}:")
                    print_board(board, new_positions=[(row, col)])  # Highlight the new number
                    time.sleep(0.5)  # Delay to visualize the step

                # Recursively attempt to solve the next cell (deep-first).
                if dfs(board, next_row, next_col):
                    return True  # Puzzle solved

                # Backtrack: If no solution found, reset the current cell.
                board[row][col] = 0

        # If no valid number can be placed, return False to backtrack.
        return False

    step_count = 0  # Initialize step counter
    solved_board = [row[:] for row in board]  # Create a copy of the board
    return solved_board if dfs(solved_board, 0, 0) else None  # Call DFS from the start


def solve_ucs(board: Board, show_steps: bool = False) -> Optional[Board]:
    """
    Solve Sudoku using UCS with optional step display.
    
    Args:
        board: The Sudoku board to solve.
        show_steps: Whether to show each step of the solution.

    Returns:
        The solved Sudoku board if a solution is found, None otherwise.
    """
    import heapq  # Import heapq for the priority queue (min-heap)

    # Initialize a priority queue for UCS.
    # Each element in the queue is a tuple: (cost, board, row, col)
    # Start at the top-left corner of the board (0, 0) with initial cost 0.
    queue = [(0, board, 0, 0)]  # The cost is 0 initially
    step_count = 0  # Counter to track the number of steps

    # Loop until the queue is empty.
    while queue:
        # Pop the element with the lowest cost (UCS explores least costly paths first).
        _, current_board, row, col = heapq.heappop(queue)

        # If we have reached the end of the board (row 9), the puzzle is solved.
        if row == 9:
            print()
            print(f"Total Cost: {step_count}")  # Display total steps taken
            return current_board  # Return the solved board

        # Move to the next column. If at the end of the row, move to the next row.
        next_row, next_col = (row, col + 1) if col < 8 else (row + 1, 0)

        # If the current cell already has a number, move to the next cell.
        if current_board[row][col] != 0:
            heapq.heappush(queue, (0, current_board, next_row, next_col))
        else:
            # Try placing each number from 1 to 9 in the current empty cell.
            for num in range(1, 10):
                # Check if placing 'num' in the current cell is valid.
                if is_valid(current_board, row, col, num):
                    # Create a copy of the board to avoid modifying the original.
                    new_board = [r[:] for r in current_board]
                    new_board[row][col] = num  # Place the number in the current cell

                    # Push the updated board and next position onto the priority queue.
                    # The cost remains 0 because each step has equal cost.
                    heapq.heappush(queue, (0, new_board, next_row, next_col))

                    # Show the current step if enabled.
                    step_count += 1  # Increment the step counter
                    if show_steps:
                        print(f"\nStep {step_count}:")
                        print_board(new_board, new_positions=[(row, col)])  # Highlight the new number
                        time.sleep(0.5)  # Add a delay to visualize the step

    # If the queue is exhausted and no solution is found, return None.
    return None

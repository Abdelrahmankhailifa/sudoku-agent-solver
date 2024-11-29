from solving_algorithms import solve_bfs, solve_dfs, solve_ucs, print_board
from board_generator import generate_sudoku_puzzle


def main():
    print()
    print()
    print("   ▄████████ ███    █▄  ████████▄   ▄██████▄     ▄█   ▄█▄ ███    █▄          ▄████████  ▄██████▄   ▄█        ▄█    █▄     ▄████████    ▄████████ ")
    print("  ███    ███ ███    ███ ███   ▀███ ███    ███   ███ ▄███▀ ███    ███        ███    ███ ███    ███ ███       ███    ███   ███    ███   ███    ███ ")
    print("  ███    █▀  ███    ███ ███    ███ ███    ███   ███▐██▀   ███    ███        ███    █▀  ███    ███ ███       ███    ███   ███    █▀    ███    ███ ")
    print("  ███        ███    ███ ███    ███ ███    ███  ▄█████▀    ███    ███        ███        ███    ███ ███       ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ ")
    print("▀███████████ ███    ███ ███    ███ ███    ███ ▀▀█████▄    ███    ███      ▀███████████ ███    ███ ███       ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ")
    print("         ███ ███    ███ ███    ███ ███    ███   ███▐██▄   ███    ███               ███ ███    ███ ███       ███    ███   ███    █▄  ▀███████████ ")
    print("   ▄█    ███ ███    ███ ███   ▄███ ███    ███   ███ ▀███▄ ███    ███         ▄█    ███ ███    ███ ███▌    ▄ ███    ███   ███    ███   ███    ███ ")
    print(" ▄████████▀  ████████▀  ████████▀   ▀██████▀    ███   ▀█▀ ████████▀        ▄████████▀   ▀██████▀  █████▄▄██  ▀██████▀    ██████████   ███    ███ ")
    print("                                                ▀                                                 ▀                                   ███    ███ ")
    print()
    print("By Khaled Hesham and Abdelrahman Haitham")
    print()
    print()

    print("Select puzzle difficulty (easy=30, medium=40, hard=50):")
    difficulty = input("Enter the number of empty cells (default is 40): ").strip()
    difficulty = int(difficulty) if difficulty.isdigit() else 40

    board = generate_sudoku_puzzle(difficulty)

    print()
    print("Generated Sudoku Puzzle:")
    print_board(board)

    print("\nChoose the solving algorithm:")
    print("1. BFS (Breadth-First Search)")
    print("2. DFS (Depth-First Search)")
    print("3. UCS (Uniform Cost Search)")
    print("4. All algorithms")

    choice = input("Enter your choice (1/2/3/4): ").strip()

    show_steps = input("Show steps? (y/n): ").strip().lower() == "y"

    if choice == "1" or choice == "4":
        print("\nSolving with BFS:")
        solved_bfs = solve_bfs(board, show_steps=show_steps)
        if solved_bfs:
            print("\nSolved Board:")
            print_board(solved_bfs)
        else:
            print("No solution found with BFS.")

    if choice == "2" or choice == "4":
        print("\nSolving with DFS:")
        solved_dfs = solve_dfs(board, show_steps=show_steps)
        if solved_dfs:
            print("\nSolved Board:")
            print_board(solved_dfs)
        else:
            print("No solution found with DFS.")

    if choice == "3" or choice == "4":
        print("\nSolving with UCS:")
        solved_ucs = solve_ucs(board, show_steps=show_steps)
        if solved_ucs:
            print("\nSolved Board:")
            print_board(solved_ucs)
        else:
            print("No solution found with UCS.")


if __name__ == "__main__":
    main()
    """
     _   ,           _       
    ' ) /  /        //      /
     /-<  /_  __.  // _  __/ 
    /   )/ /_(_/|_</_</_(_/_ 
       __             _                               
      /  ) /    /    //          /                    
     /--/ /____/ _  // __  __.  /_  ______  __.  ____ 
    /  (_/_)(_/_</_</_/ (_(_/|_/ /_/ / / <_(_/|_/ / <_
                     
    """

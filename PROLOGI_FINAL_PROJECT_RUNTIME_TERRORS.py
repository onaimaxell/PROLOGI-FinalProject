
"""
    1. Help menu
    2. Main loop
    3.

    To do:
    AI Opponent (Easy/Hard Mode)
    Scoreboard System
    Custom Board Size <---??
    Power-ups & Special Moves (Undo Move, Double Turn) <---??
"""

def print_menu():
    print("1. Help")
    print("2. Play game")
    print("3. Quit")

def print_help():
    print("1. Help Section:")
    print("2. Players take turns putting their marks in empty squares")
    print("3. The first player to get 3 of her marks in a row (vertical, horizontal, or diagonally) is the winner.")
    print("4. When all squares are filled, the game is over. If no player has 3 marks in a row, the game ends in a tie.")
    print("5. Use the corresponding number on the grid to place your marks")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")

def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False
    
def get_valid_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move in range(1, 10) and board[move - 1] not in ("X", "O"):
                return move - 1
            print("Invalid move! Try again.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")

def print_board(board):
    for row, i in enumerate(board):
        print(" | ".join(i))
        if row < 2:
            print("---------")


def play_game():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    current_player = 'X'
    moves = 0

    while moves < 9:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        move = get_valid_move(board) # <----------------- CONTINUE HERE
    print("Invalid number!")

def main():
    while True:
        print_menu()
        choice = int(input("Choose an option: "))

        if choice == 1:
            print_help()
        elif choice == 2:
            play_game()
        elif choice == 3:
            print("Thank you for playing our game!")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()

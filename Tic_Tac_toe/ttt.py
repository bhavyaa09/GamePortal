import time
import random
import pyttsx3
from colorama import Fore, Style, init # type: ignore

init(autoreset=True)

engine = pyttsx3.init()

def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

def print_board(board):
    for i, row in enumerate(board):
        colored_row = ""
        for j, cell in enumerate(row):
            if j % 3 == 0:
                colored_row += f"{Style.BRIGHT}|"
            if cell == 'X':
                colored_row += f"{Fore.GREEN} {cell} {Style.RESET_ALL}"
            elif cell == 'O':
                colored_row += f"{Fore.RED} {cell} {Style.RESET_ALL}"
            else:
                colored_row += f"{Fore.WHITE} {cell} {Style.RESET_ALL}"
            if j == 2:
                colored_row += f"{Style.BRIGHT}|"
            else:
                colored_row += "|"
        print(colored_row)
        if i == 2:
            print("-" * 13)
        else:
            print("-" * 13)


def check_win(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_tie(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def get_user_move(board, player_name):
    while True:
        try:
            text_to_speech(f"Enter your move {player_name}")
            move = int(input(Fore.MAGENTA + Style.BRIGHT +f"{player_name}'s Enter your move (1-9): "))
            if 1 <= move <= 9 and board[(move - 1) // 3][(move - 1) % 3] == ' ':
                return move
            else:
                text_to_speech("Please enter a valid and unoccupied position (1-9)")
                print(Fore.RED+ Style.BRIGHT + "Please enter a valid and unoccupied position (1-9).")
        except ValueError:
            text_to_speech("Please enter a valid number")
            print(Fore.RED+ Style.BRIGHT +"Please enter a valid number.")

def get_computer_move(board):
    print()
    print("-"*13)
    while True:
        move = random.randint(1, 9)
        row = (move - 1) // 3
        col = (move - 1) % 3
        if board[row][col] == ' ':
            return move

def welcome_message():
    print(Fore.YELLOW + Style.BRIGHT + "Welcome to Tic Tac Toe!")
    print(f"{Fore.YELLOW}{Style.BRIGHT}-"*25)
    text_to_speech("Welcome to Tic Tac Toe!")

def countdown():
    for i in range(3, 0, -1):
        print(f"Starting game in {i}...")
        time.sleep(1)

def play_game():

    welcome_message()

    text_to_speech("Are you ready to start the game?")
    ready = input("\nAre you ready to start the game? (yes/no): ").lower()
    if ready == "yes":
        print(Fore.YELLOW+ Style.BRIGHT+ "\nAll The Best!")
        text_to_speech("All the best")
        countdown()
    else:
        print(Fore.LIGHTRED_EX + Style.BRIGHT+ "Okay, whenever you're ready, let's get started!")
        text_to_speech("whenever you're ready, let's get started! till then bbye")
        return

    text_to_speech("Select mode - '1' for Player vs Player, '2' for Player vs Computer")
    mode = input(Fore.YELLOW + Style.BRIGHT+ "Select mode - '1' for Player vs Player, '2' for Player vs Computer: ")
    while mode not in ['1', '2']:
        text_to_speech("Invalid input! Select mode - '1' for Player vs Player, '2' for Player vs Computer")
        mode = input(Fore.RED+ Style.BRIGHT +"Invalid input! Select mode - '1' for Player vs Player, '2' for Player vs Computer: ")
    
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print_board(board)
    
    if mode == '1':
        text_to_speech("Enter name for Player 1")
        player1 = input(Fore.CYAN + Style.BRIGHT + "Enter name for Player 1: ")
        text_to_speech("Enter name for Player 2")
        player2 = input(Fore.MAGENTA + Style.BRIGHT + "Enter name for Player 2: ")
    else:
        player1 = "Player"
        player2 = "Computer"

    current_player = 'X'
    while True:
        if mode == '1' or current_player == 'X':
            print(f"\n{Fore.CYAN if current_player == 'X' else Fore.GREEN}{player1 if current_player == 'X' else player2}'s turn:")
            move = get_user_move(board, player1 if current_player == 'X' else player2)
        else:
            print(f"\n{Fore.MAGENTA}{player2 if mode == '1' else 'Computer'}'s turn:")
            move = get_computer_move(board)

        row = (move - 1) // 3
        col = (move - 1) % 3
        board[row][col] = current_player
        print_board(board)

        if check_win(board, current_player):
            if mode == '1':
                print(f"{Fore.GREEN} {Style.RESET_ALL} {player1 if current_player == 'X' else player2} wins!")
            else:
                print( Fore.GREEN + Style.BRIGHT + "\nBravo! You win.." if current_player == 'X' else Fore.RED+ Style.BRIGHT+ "\nOOps! Computer wins!\nBetter luck next time!")
            break
        elif check_tie(board):
            print(Fore.CYAN + Style.BRIGHT +"\nIt's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()

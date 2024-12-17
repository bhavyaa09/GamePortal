import time
import random
import pyttsx3 
from KBC import kbc
from Tic_Tac_toe import ttt
from Hangman import hangman
from Rock_paper_cissor import rpc
from Black_jack import black_jack
from colorama import init, Fore, Style

init(autoreset=True)

engine = pyttsx3.init()

def text_to_speak(text):
    engine.say(text)
    engine.runAndWait()

def display_menu():
    text_to_speak("You can now select one of the game options to play")
    print(Fore.MAGENTA + "="*40)
    print(Fore.MAGENTA +"║" + " "*(40//2-7) + "Game Options" + " "*(40//2-6) + "║")
    print(Fore.MAGENTA +"="*40)
    print("1. KBC (Kaun Banega Crorepati)")
    print("2. Tic Tac Toe")
    print("3. Blackjack")
    print("4. Rock Paper Scissors")
    print("5. Hangman")
    print(Fore.MAGENTA +"="*40)

def start_game(game):

    if game == 1:
        print("Starting KBC...\n")
        text_to_speak("Starting KBC")
        time.sleep(1)
        kbc.main()

    elif game == 2:
        print("Starting Tic Tac Toe...\n")
        text_to_speak("Starting Tic Tac Toe")
        time.sleep(1)
        ttt.play_game()

    elif game == 3:
        print("Starting Blackjack...\n")
        text_to_speak("Starting Black Jack")
        time.sleep(1)
        black_jack.play_blackjack()

    elif game == 4:
        print("Starting Rock Paper Scissors...\n")
        text_to_speak("Starting Rock Paper Scissors")
        time.sleep(1)
        rpc.play_game()

    elif game == 5:
        print("Starting Hangman...\n")
        text_to_speak("Starting Hangman")
        time.sleep(1)
        hangman.play_game()

    else:
        print(F"{Fore.RED}{Style.BRIGHT}Invalid selection!")

def select_game():

    display_menu()

    start_time = time.time()

    while True:

        text_to_speak("Enter the number of the game you want to play")
        selection = input("Enter the number of the game you want to play: ")

        if selection.isdigit() and 1 <= int(selection) <= 5:
            start_game(int(selection))
            break

        elif time.time() - start_time > 30:
            game = random.randint(1, 5)
            print("You took too long to decide! Starting a random game...")
            start_game(game)
            break

        else:
            text_to_speak("Invalid selection! Please enter a number between 1 and 5")
            print(f"{Fore.RED}{Style.BRIGHT}Invalid selection! Please enter a number between 1 and 5.")

def game_portal():

    try:
        print(f"{Fore.YELLOW}{Style.BRIGHT}-"*31)
        print(f"{Fore.YELLOW}{Style.BRIGHT}| Welcome to our Game Portal! |")
        print(f"{Fore.YELLOW}{Style.BRIGHT}-"*31)
        text_to_speak("Welcome to our Game Portal!")

        text_to_speak("Enter your name")
        name = input("Enter your name : ")

        print(f"Hello {name}!")
        text_to_speak(f"Hello {name} I hope you are doing great!")

        while True:
            select_game()
            text_to_speak("Do you want to play another game?")
            play_again = input(f"\n{Fore.BLUE}{Style.DIM}Do you want to play another game? (yes/no): ").lower()
            if play_again != 'yes':
                print(f"{Fore.CYAN}{Style.BRIGHT}Thanks for playing! See you Again!")
                text_to_speak("Thanks for playing! See you Again!")
                break

    except KeyboardInterrupt:
        print(f"\n{Fore.RED}{Style.BRIGHT}Keyboard interupt detected\nThank you for playing! See you again1")
        text_to_speak("Keyboard interrupt detected. Thank you for playing! See you again!")

game_portal()

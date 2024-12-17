import time
import random
import pyttsx3
from colorama import init, Fore, Style # type: ignore

init(autoreset=True)

engine = pyttsx3.init()

def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

def welcome_message():
    print(Fore.YELLOW + Style.BRIGHT + "Welcome to Rock paper scissor")
    print(f"{Fore.YELLOW}{Style.BRIGHT}-"*30)
    text_to_speech("Welcome to Rock paper scissor")
    text_to_speech("You'll be playing against the computer.")
    print(Fore.YELLOW + Style.BRIGHT + "\nYou'll be playing against the computer.")
    print(Fore.YELLOW + Style.BRIGHT + "\nEnter 'r' for Rock, 'p' for Paper, and 's' for Scissors.")
    text_to_speech("Enter 'r' for Rock, 'p' for Paper, and 's' for Scissors.")

def get_user_choice():
    user_choice = input("Your choice: ").lower()
    while user_choice not in ['r', 'p', 's']:
        text_to_speech("Invalid choice! Please enter 'r', 'p', or 's'")
        print(Fore.RED + "Invalid choice! Please enter 'r', 'p', or 's'.")
        user_choice = input("Your choice: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['r', 'p', 's'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'r' and computer_choice == 's') or (user_choice == 'p' and computer_choice == 'r') or (user_choice == 's' and computer_choice == 'p'):
        return "You win!"
    else:
        return "Computer wins!"

def colorize_ascii(ascii_art, color):
    return "\n".join([color + line for line in ascii_art.split("\n")])

def display_choice(choice):
    if choice == 'r':
        return colorize_ascii("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)""", Fore.GREEN)
    elif choice == 'p':
        return colorize_ascii("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)""", Fore.BLUE)
    elif choice == 's':
        return colorize_ascii("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)""", Fore.YELLOW)

def display_score(result, scores, user_choice, computer_choice):
    print()
    print("Your choice:")
    print(display_choice(user_choice))
    print("Computer's choice:")
    print(display_choice(computer_choice))
    if result == "You win!":
        text_to_speech("Bravo You won")
        print(Fore.GREEN + Style.BRIGHT + "BRAVO! You win!🎉")
    elif result == "Computer wins!":
        text_to_speech("OOps You lost this time")
        print(Fore.RED + Style.BRIGHT + "OOPS! Computer wins!💔")
    else:
        text_to_speech("OO Its a tie")
        print(Fore.YELLOW + Style.BRIGHT + "It's a tie!")
    print(Fore.CYAN + Style.BRIGHT + f"Your score: {scores['user']}")
    print(Fore.CYAN + Style.BRIGHT + f"Computer's score: {scores['computer']}")

def countdown():
    for i in range(3, 0, -1):
        print(f"Starting game in {i}...")
        time.sleep(1)

def play_game():

    welcome_message()

    text_to_speech("Are you ready to start the game")
    ready = input("\nAre you ready to start the game? (yes/no): ").lower()
    
    if ready == "yes":
        print(Fore.YELLOW+ Style.BRIGHT+ "\nAll The Best!")
        text_to_speech("All the best")
        countdown()
    else:
        text_to_speech("Okay, whenever you're ready, let's get started! till then bbye")
        print(Fore.LIGHTRED_EX + Style.BRIGHT+ "Okay, whenever you're ready, let's get started!")
        return
    
    scores = {'user': 0, 'computer': 0}

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        if result == "You win!":
            scores['user'] += 1
        elif result == "Computer wins!":
            scores['computer'] += 1
        display_score(result, scores, user_choice, computer_choice)

        text_to_speech("Do you want to play again this game")
        play_again = input(Fore.MAGENTA + Style.BRIGHT+ "Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
        
if __name__ == "__main__":
    play_game()

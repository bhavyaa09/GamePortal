import time
import string
import random
import pyttsx3
from colorama import init, Fore, Style # type: ignore

init(autoreset=True)

engine = pyttsx3.init()

def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

def welcome_message():
    print(Fore.YELLOW + Style.BRIGHT + "Welcome to Hangman!")
    print(f"{Fore.YELLOW}{Style.BRIGHT}-"*25)
    text_to_speech("Welcome to Hangman!")
    
def load_word():
    word_list = ["mango", "guitar", "orange", "database", "strawberry", "friction", "lavender", "rainbow","castle"]  
    return random.choice(word_list).lower()

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def draw_hangman(attempts_left, max_attempts):
    hangman_parts = [
        Fore.BLUE + Style.BRIGHT + """
        ________
        |    |
        |    
        |    
        |    
        |   
      __|__  
        """,
        Fore.BLUE + Style.BRIGHT + """
        ________ 
        |    |
        |    O
        |    
        |    
        |   
      __|__  
        """,
        Fore.BLUE + Style.BRIGHT + """
         _______
        |    |
        |    O
        |    |
        |    
        |   
      __|__  
        """,
        Fore.BLUE + Style.BRIGHT + """
         _______ 
        |    |
        |    O
        |   /|
        |    
        |   
      __|__  
        """,
        Fore.BLUE + Style.BRIGHT + """
        ______ 
        |    |
        |    O
        |   /|\\
        |    
        |   
      __|__  
        """,
        Fore.BLUE + Style.BRIGHT + """
        ______ 
        |    |
        |    O
        |   /|\\
        |   / 
        |   
      __|__  
        """,
        Fore.BLUE + Style.BRIGHT + """
        ______ 
        |    |
        |    O
        |   /|\\
        |   / \\
        |   
      __|__  
        """
    ]
    print(hangman_parts[max_attempts - attempts_left])

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
      text_to_speech("Okay whenevver you are ready lets get started till then bbye!")
      return

    word_to_guess = load_word()
    guessed_letters = []
    max_attempts = 6
    attempts_left = max_attempts

    print("Guess the word:")
    text_to_speech("Guess the word in 6 attempts")

    while True:
        draw_hangman(attempts_left, max_attempts)
        print(Fore.GREEN + display_word(word_to_guess, guessed_letters))
        print(Fore.YELLOW + f"Attempts left: {attempts_left}")

        if "_" not in display_word(word_to_guess, guessed_letters):
            print(Fore.GREEN + "Congratulations! You won!!")
            text_to_speech("ohoo Congratulations you won")
            break

        if attempts_left == 0:
            print(Fore.RED + "Sorry, you lost! Better luck next time")
            text_to_speech("OOps you lost Better luck next time")
            print(Fore.MAGENTA + "The word was:", word_to_guess)
            break
        
        text_to_speech("Enter a letter")
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print(Fore.RED + "Please enter a single letter.")
            text_to_speech("Please enter single letter")
            continue

        if guess in guessed_letters:
            print(Fore.RED + "You have already guessed that letter.")
            text_to_speech("oo you already gussed this letter")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts_left -= 1
            print(Fore.RED + f"Oops! {attempts_left} attempts left.")
            text_to_speech(f"oops {attempts_left} attempts lefts")

if __name__ == "__main__":
    play_game()

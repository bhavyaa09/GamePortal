import time
import random
import pyttsx3
import threading
from . import sound1 
from . import lifeline 
from . import questions
from . import timer1 as timer
from colorama import Fore, Style

engine = pyttsx3.init()

def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

def welcome_message():
    print(Fore.YELLOW + Style.BRIGHT + "Welcome to Kaun Banega Crorepati!")
    print(f"{Fore.YELLOW}{Style.BRIGHT}-"*40)
    text_to_speech("Welcome to Kaun Banega Crorepati!")

def countdown():
    for i in range(3, 0, -1):
        print(f"Starting game in {i}...")
        time.sleep(1)

def main():

    welcome_message()

    text_to_speech("Are you ready to start the game")
    ready = input("\nAre you ready to start the game? (yes/no): ").lower()
    if ready == "yes":
        print(Fore.YELLOW+ Style.BRIGHT+ "\nAll The Best!")
        text_to_speech("All the best")
        countdown()
    else:
        print(Fore.LIGHTRED_EX + Style.BRIGHT+ "Okay, whenever you're ready, let's get started!")
        text_to_speech("Okay lets get started whenever you want till then bbye")
        return

    prize_money = 0
    lifeline_used = False

    question = questions.get_questions()
    random.shuffle(question)

    text_to_speech("Displaying question")

    for number, question in enumerate(question):
        print(f"{Fore.MAGENTA}{Style.DIM}\nQuestion{1+number}: {question['question']}")
        for option in question['options']:
            print(option)

        sound1.stop_event = threading.Event()
        timer_thread = threading.Thread(target=timer.countdown_timer, args=(60, sound1.stop_event))
        timer_thread.start()

        text_to_speech("Enter option number to answer or you can type l for lifeline and q to quit the game")
        user_input = input(Fore.CYAN + Style.DIM + "Enter your answer (option number), 'L' to use a lifeline, or 'Q' to quit the game: ")

        if sound1.stop_event.is_set():
            print("Time's Up!!")
            print(f"{Fore.GREEN}{Style.BRIGHT}Final Prize Money: {prize_money}")
            break

        sound1.stop_event.set() 
        timer_thread.join()

        if user_input.lower() == 'q':
            print(f"{Fore.RED}{Style.DIM}You decided to quit a game.")
            text_to_speech("You decided to quit your game")
            break

        elif user_input.lower() == 'l':
            options = lifeline.use_lifeline(question, lifeline_used)

            if options:
                lifeline_used = True
                print(f"Options available: {options}")
                user_input = input(Fore.CYAN + Style.DIM +"Enter your answer(option number): ")

            else:
                text_to_speech("You already used your lifeline before can't use now")
                user_input = input(Fore.CYAN + Style.DIM +"Enter your answer (option number): ")

        try:
            user_answer = int(user_input)

        except ValueError:
            print(Fore.RED + Style.BRIGHT+"Invalid input! Ending the game.")
            text_to_speech("Input is not correct sorry you are out of the game")
            break

        if user_answer == question["answer"]:
            print(Fore.GREEN + Style.BRIGHT + "Correct answer!")
            text_to_speech("Correct answer")
            prize_money = questions.prize_levels[number]
            print(f"{Fore.BLUE}{Style.BRIGHT}Prize Money: {prize_money}")
            text_to_speech(f"You won {prize_money} rupees")

        else:
            print(Fore.RED + Style.BRIGHT+ "Wrong answer!")
            text_to_speech("OO Wrong answer Exiting from the game")
            if prize_money >= questions.stage_two:
                prize_money = questions.stage_two
            elif prize_money >= questions.stage_one:
                prize_money = questions.stage_one
            else:
                prize_money = 0
            break

    print(f"{Fore.BLUE}{Style.DIM}Final Prize Money: {prize_money}")
    text_to_speech(f"Your final prize money is {prize_money} rupees")
    print(f"{Fore.CYAN}{Style.BRIGHT}Thank you for playing!")
    text_to_speech("Thank you for playing See you again")

if __name__ == "__main__":
    main()

import time
import random
import pyttsx3
from colorama import init, Fore, Style # type: ignore


init(autoreset=True)

engine = pyttsx3.init()

def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            value += 10
        elif card == 'A':
            num_aces += 1
            value += 11
        else:
            value += int(card)

    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    
    return value

def deal_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)

def display_hands(player_hand, dealer_hand, show_dealer_card):
    print("\n" + Fore.CYAN + "╔════════════════════════════════════════════════╗")
    print("║" + Fore.YELLOW + "Your hand: " + Fore.WHITE + ', '.join(player_hand) + " "*(46 - len(', '.join(player_hand))))
    print("║" + Fore.YELLOW + "Dealer's hand: " + Fore.WHITE + (', '.join(dealer_hand) if show_dealer_card else dealer_hand[0]) + " "*(46 - len(dealer_hand) - 1))
    print("╚════════════════════════════════════════════════╝" + Style.RESET_ALL)

def display_winner(player_value, dealer_value):

    if player_value > 21:
        print(Fore.RED + "\nYou busted! Dealer wins!", Style.RESET_ALL)
        print("Better luck next time")
        text_to_speech("OO You lost Better luck next time")

    elif dealer_value > 21:
        print(Fore.GREEN + "\nDealer busted! You win!", Style.RESET_ALL)
        text_to_speech("Congratulation You Won")

    elif player_value == dealer_value:
        print(Fore.YELLOW + "\nIt's a tie!", Style.RESET_ALL)
        text_to_speech("OO its a tie")

    elif player_value > dealer_value:
        print(Fore.GREEN + "\nBravo!! You win!", Style.RESET_ALL)
        text_to_speech("Congratulation You Won")
    else:
        print(Fore.RED + "\nOOps!! Dealer wins!", Style.RESET_ALL)
        print("Better luck next time")
        text_to_speech("OO You lost Better luck next time")

def countdown():
    for i in range(3, 0, -1):
        print(f"\nStarting game in {i}...")
        time.sleep(1)

def play_blackjack():

    print(Fore.CYAN + "\n" + "="*50)
    print("║" + " "*(50//2-10) + "Welcome to Blackjack!" + " "*(50//2-10))
    print(Fore.CYAN +"="*50)
    text_to_speech("welcome to black jack")

    print(f"{Fore.MAGENTA}{Style.BRIGHT}All the best for your game.")
    text_to_speech("all the best for your game")

    text_to_speech("Are you ready to start the game?")
    ready = input("\nAre you ready to start the game? (yes/no): ").lower()

    if ready == "yes":
        print(Fore.YELLOW+ Style.BRIGHT+ "\nGet as close to 21 as you can without going over!")
        text_to_speech("Get as close to 21 as you can without going over!")
        countdown()

    else:
        print(Fore.LIGHTRED_EX + Style.BRIGHT+ "Okay, whenever you're ready, let's get started!")
        text_to_speech("whenever you're ready, let's get started! till then bbye")
        return
    
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    display_hands(player_hand, dealer_hand, False)

    while True:

        text_to_speech("Do you want to hit or stand? ")
        choice = input(Fore.MAGENTA + Style.BRIGHT +"\nDo you want to hit or stand? (h/s): ").strip().lower()

        if choice == 'h':
            player_hand.append(deal_card())
            display_hands(player_hand, dealer_hand, False)
            player_value = calculate_hand_value(player_hand)

            if player_value >= 21:
                break

        elif choice == 's':
            break

        else:
            text_to_speech("Invalid choice! Please enter 'h' to hit or 's' to stand.")
            print(f"{Fore.RED}{Style.BRIGHT}Invalid choice! Please enter 'h' to hit or 's' to stand.")

    dealer_value = calculate_hand_value(dealer_hand)

    while dealer_value < 17:
        dealer_hand.append(deal_card())
        dealer_value = calculate_hand_value(dealer_hand)

    display_hands(player_hand, dealer_hand, True)

    player_value = calculate_hand_value(player_hand)
    display_winner(player_value, dealer_value)

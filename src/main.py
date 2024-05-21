import random
import time
from termcolor import colored
import sys
from config import FILEPATH
from text import won, lost, replay, title, boxes

# views ##############


def print_menu():
    '''displays the menu view for the player'''
    print("Let's play Wordle!")
    print("Type a 5 letter word and hit enter!\n")


def read_random_word():
    '''reads a random word from the file of words'''
    with open(FILEPATH, 'r') as file:
        words = file.read().splitlines()
        return random.choice(words)


def get_five_characters():
    '''takes player's guess input'''
    errors = 0
    while True:
        user_input = input()
        if len(user_input) == 5:
            break
        print("Error: Enter a five letter word!")
        time.sleep(2)
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        errors += 1
        if errors > 3:
            print("Too many incorrect inputs, Goodbye!")
            exit()
    return user_input

# Main Function ################


def main():
    lost_game = False
    play_again = ""
    print(title("Welcome to ......."))
    while 'q' not in play_again:
        print_menu()
        word = read_random_word().lower()

        for attempt in range(1, 7):
            guess = get_five_characters().lower()
            temp = []

            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')

            for i in range(5):
                if guess[i] == word[i]:
                    temp.append(colored(guess[i], 'green'))
                elif guess[i] in word:
                    temp.append(colored(guess[i], 'yellow'))
                else:
                    temp.append(colored(guess[i], 'white'))
            print(boxes(temp))
            if guess == word:
                print(colored(won(attempt), 'red'))
                break
            if guess != word and attempt == 6:
                lost_game = True
        if lost_game:
            print(lost())
            for i in range(5):
                print("The wordle was." + i*".")
                time.sleep(1)
                sys.stdout.write('\x1b[1A')
                sys.stdout.write('\x1b[2K')
            print(f"The wordle was {word}")
            time.sleep(2)

        play_again = input(replay())
    print(title("Thanks for playing"))


if __name__ == "__main__":
    main()

import random
import time
import sys
from termcolor import colored
from config import FILEPATH
from text import won, lost, replay

############# views ##############


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

################ Main Function ################


def main():
    lost_game = False
    play_again = ""
    while play_again != 'q':
        print_menu()
        word = read_random_word()

        for attempt in range(1, 7):
            guess = get_five_characters().lower()

            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')

            for i in range(5):
                if guess[i] == word[i]:
                    print(colored(guess[i], 'green'), end="")
                elif guess[i] in word:
                    print(colored(guess[i], 'yellow'), end="")
                else:
                    print(guess[i], end="")
            print()
            if guess == word:
                print(colored(won(attempt), 'red'))
                break
            if attempt == 6:
                lost_game = True
        if lost_game:
            print(lost())
        play_again = input(replay())


if __name__ == "__main__":
    main()

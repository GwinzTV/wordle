import random
import sys
import curses
from termcolor import colored
from config import FILEPATH

############# views ##############


def print_menu():
    print("Let's play Wordle!")


def read_random_word():
    with open(FILEPATH, 'r') as file:
        words = file.read().splitlines()
        return random.choice(words)


def get_five_characters(stdscr):
    curses.echo()
    stdscr.addstr("Type a 5 letter word and hit 'Enter': ")
    user_input = ""
    while len(user_input) < 5:
        ch = stdscr.get_wch()
        if isinstance(ch, str) and len(ch) == 1 and ch.isprintable():
            user_input += ch
            stdscr.addch(ch)
    return user_input

################ Main Function ################


def main():
    print_menu()
    word = read_random_word()

    for attempt in range(1, 7):
        guess = curses.wrapper(get_five_characters).lower()

        for i in range(5):
            if guess[i] == word[i]:
                print(colored(guess[i], 'green'), end="")
            elif guess[i] in word:
                print(colored(guess[i], 'yellow'), end="")

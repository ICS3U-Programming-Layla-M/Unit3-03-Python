#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: May, 11, 2021
# This program asks the user to input a number between 0 and 9,
# generates a random number and displays a message depending
# on if the guess is the same as the random number or not

import random

# get the user guess
number = int(input("Guess what number I am thinking of between 0 and 9: "))


def main():
    # define variable
    correct_guess = random.randint(0, 9)

    # check if guess is correct and display message
    # depending on if it's right or wrong
    if (number == correct_guess):
        print("You guessed correctly!")
    else:
        print("You guessed wrong. The correct answer was: {}\
        ". format(correct_guess))


if __name__ == "__main__":
    main()

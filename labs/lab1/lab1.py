#!/usr/bin/env python3

# Imports
import os
import sys
import random

# Functions
def ask_for_number() -> int:
    '''
    Function to ask user to input a number. Returns the number when the input is correct.
    '''
    def check_input(user_input: str, desired_input: str) -> bool:
        '''
        Internal function to validate input. Returns True/False if input is valid
        '''
        return (user_input == desired_input)

    N = random.randint(1, 10)

    number = input(f"Input the number {N}: ")

    # recursively call this function if input is invalid
    if not check_input(number, str(N)):
        N = ask_for_number()

    # return N
    return N

# Executable portion
if __name__ == "__main__":

    # Clear terminal screen
    if os.name == "posix":
        # posix clear terminal command
        os.system("clear")
    elif os.name == "nt":
        # windows clear terminal command
        os.system("cls")

    # Get number from user. Will only return the value when the correct input is received
    N = ask_for_number()

    print(f"\nPrinting {N} float numbers from 0-100:\n")

    # Print N random floats in between 0-100
    for i in range(N):
        print(f"Number {i+1}:", random.random() * 100)

    # print thank you message
    print("\nThank you :)\n")

    # terminate program
    sys.exit(0)

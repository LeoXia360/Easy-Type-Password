#!/usr/bin/env python

import argparse
import sys
import click
import random


LEFT_SIDE_VOWELS = ['e', 'a']
LEFT_SIDE_CONSONANTS = ['r', 't', 's', 'd', 'f', 'g', 'v', 'w']
LEFT_SIDE_NUMBERS = ['1', '2', '3', '4', '5']
#LEFT_SIDE_SPECIAL = ['!', '@', '#', '$', '%']

RIGHT_SIDE_VOWELS = ['u', 'i', 'o']
RIGHT_SIDE_CONSONANTS = ['p', 'h', 'j', 'k', 'l', 'n', 'y']
RIGHT_SIDE_NUMBERS = ['7', '8', '9', '0']
#LEFT_SIDE_SPECIAL = ['^', '&', '*', '-', '+']

if __name__ == "__main__":
    password_length = raw_input("Enter desired password length: ")
    password_length = int(password_length)
    #allow_special_characters = click.confirm('Do you want to allow special characters in your password?', default=True)
    
    user_accepted_password = False
    while (not user_accepted_password):
        password = ''
        # password_length - 2 for special characters
        for char_position in xrange(0, password_length - 2):
            if (char_position % 4 == 0):
                password = password + LEFT_SIDE_CONSONANTS[random.randint(-1, len(LEFT_SIDE_CONSONANTS) - 1)]
            elif (char_position % 2 == 0):
                password = password + LEFT_SIDE_VOWELS[random.randint(-1, len(LEFT_SIDE_VOWELS) - 1)]
            elif (char_position % 3 == 0):
                password = password + RIGHT_SIDE_CONSONANTS[random.randint(-1, len(RIGHT_SIDE_CONSONANTS) - 1)]
            elif(char_position % 1 == 0):
                password = password + RIGHT_SIDE_VOWELS[random.randint(-1, len(RIGHT_SIDE_VOWELS) - 1)]
        password = password + LEFT_SIDE_NUMBERS[random.randint(-1, len(LEFT_SIDE_NUMBERS) - 1)]
        password = password + RIGHT_SIDE_NUMBERS[random.randint(-1, len(RIGHT_SIDE_NUMBERS) - 1)]
        print password
        user_accepted_password = click.confirm('Are you happy with the generated password?', default=True)

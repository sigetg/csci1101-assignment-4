# Write a program that plays a guessing game with the user.  Specifically, your
# program should randomly pick a target number between 1 and 100.  Then, ask the
# user for a guess.  You should detect and tell the user if the guess is not a
# valid guess.  Otherwise, tell the user their guess was too high or too low.
# The program should continue to prompt the user for new guesses until they get
# the correct number, telling them each time if the guess was too high, too low,
# or invalid.
#
# The random module includes many functions to generate random numbers.  You
# will use the random.randint(a, b) function to generate a random number between
# a and b, in this case between 1 and 100.  Testing your code with a random
# target number each time can be challenging.  Here are simple testing and
# debugging techniques you can use to help:
#
# Set the target to a particular number rather than a random number while
#     testing.
# Print the random target to the screen at the start of the program to verify
#     that your outputs are correct for each player guess.
#
# Obviously, be sure that you undo any such debugging changes you make before
# you complete/submit the program.
#
# Your input and output messages must conform to the following example: 
#
# Enter your guess from 1 to 100: 0
# Guesses must be between 1 and 100!
# Enter your guess from 1 to 100: 101
# Guesses must be between 1 and 100!
# Enter your guess from 1 to 100: 100
# Too high!
# Enter your guess from 1 to 100: 1
# Too low!
# Enter your guess from 1 to 100: 50
# Too low!
# Enter your guess from 1 to 100: 90
# Too high!
# Enter your guess from 1 to 100: 72
# You win!
#
# Note the order of outputs, capitalization of messages, spacing, etc.

import random

a = random.randint(1, 100)

b = int(input("Enter your guess from 1 to 100: "))
while b!=a:
    if b<1 or b>100:
        print("Guesses must be between 1 and 100!")
    elif b>a:
        print("Too high!")
    elif a>b:
        print("Too low!")  
    b = int(input("Enter your guess from 1 to 100: "))

print("You win!")

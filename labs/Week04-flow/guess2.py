# This program prompts the user to guess a number
# It will tell the user if their guess is too high or too low
# each time that they guess until they guess the right one.
# Author: Amanda Murray

import random
numberToGuess = random.randint(1, 100) # As per Q4 random number between 0 and 100 will be generated

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print ("too low")
    else:
        print ("too high")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was", numberToGuess)
# This program prompts the user to guess a number
# The program should keep prompting them to guess 
# until they guess the right one.
# Author: Amanda Murray

numberToGuess = 30

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    print ("Wrong!")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was", numberToGuess)
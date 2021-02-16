# This program asks the user to enter a number
# The program will tell them if it's even or odd
# Author: Amanda Murray

number = int (input("enter an integer:"))

if (number % 2) == 0:
    print (" {} is an even number".format(number))
else:
    print ("{} is an odd number".format(number))
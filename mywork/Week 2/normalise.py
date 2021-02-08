# normalise.py
# Lab 2.3
# This program reads in a string and strips any leading or trailing spaces
# It also converts all the letters to lower case
# The program outputs the length of the input and output strings
# Author: Amanda Murray

rawstring = input ("please enter a string:")
normalisedstring = rawstring.strip().lower()

lengthofrawstring = len (rawstring)
lengthofnormalisedstring = len (normalisedstring)

print ("that string normalised is: {}".format (normalisedstring))
print ("we reduced the input string from {} to {} characters".format (lengthofrawstring, lengthofnormalisedstring))
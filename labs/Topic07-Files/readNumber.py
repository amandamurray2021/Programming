# Q2(a)
# Write a function that reads in a number from a file that already exists (count.txt).
# Test the program by calling the function and outputting the number.
# Author: Amanda Murray

filename = "count.txt"
def readNumber ():
    with open (filename) as f:
        number = int(f.read())
        return number
# test it
num = readNumber ()
print (num)
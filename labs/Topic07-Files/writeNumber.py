# Q2(b)
# Write a function that reads in a number and overwrites the file with that number (count.txt).
# Test the program to check that the file has been changed.
# Author: Amanda Murray

filename = "count.txt"
def writeNumber(number):
    with open (filename, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))

# test it
writeNumber (3)
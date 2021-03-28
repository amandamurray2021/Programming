# Q2(c)
# Write a program that uses these two functions to count how many times the program has been run.
# Test the program to check that the number goes up each time.
# Author: Amanda Murray

filename = "count.txt"
def readNumber():
    with open (filename) as f:
        number = int(f.read())
        return number

def writeNumber():
    with open (filename, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))

#main
num = readNumber ()
num += 1
print ("We have run this program {} times".format (num))
writeNumber (num)
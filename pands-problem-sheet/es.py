# Weekly Task 7
# Write a program that reads in a text file 
# It will output the number of e's it contains
# The program will take the filename from an argument on the command line
# Author: Amanda Murray

filename = "mobydick.txt"

def readnumber(filename, number, character): # this function is reading in three arguments: the filename, the number from the text
    with open (filename, encoding ="UTF8") as f: # and the characters 'E' and 'e'
        number = (f.read()) # This reads through the file
        count = 0 # This begins the counter for what we are counting
        for character in number:
            if character == 'E': # for uppercase e's
                count +=1
            elif character == 'e': # for lowercase e's
                count += 1
        return count # return the number of uppercase and lowercase e's in the text

print (readnumber(filename, 'E', 'e')) 
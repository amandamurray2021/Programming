# Weekly Task 7
# Write a program that reads in a text file 
# It will output the number of e's it contains
# The program will take the filename from an argument on the command line
# Author: Amanda Murray


#f = open("mobydick.txt", "r")
#for e in f:
#    print (e)


filename = "mobydick.txt"
def readnumber(filename, number, character):
    with open (filename, encoding ="UTF8") as f:
        number = (f.read())
        count = 0
        for character in number:
            if character == 'E':
                count +=1
            elif character == 'e':
                count += 1
        return count

print (readnumber(filename, 'E', 'e'))
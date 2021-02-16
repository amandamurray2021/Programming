# This program reads in a student's percentage mark
# and prints out the corresponding grade
# Author: Amanda Murray

percentage = float(input("Enter the percentage: "))
# prints the percentage

if percentage < 0 or percentage > 100:
    print ("Please enter a number between 0 and 100")
elif percentage < 40: # we know it is greater than 0
    print ("Fail")
elif percentage < 50: # between 40 and 49
    print ("Pass")
elif percentage < 60: # between 50 and 59
    print ("Merit 2")
elif percentage < 70: # between 60 and 69
    print ("Merit 1")
else: # the only option left is between 70 and 100
    print ("Distinction")
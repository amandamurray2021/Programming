# This program asks the user to input any positive integer
# It outputs the successive values of the following calculation
# Author: Amanda Murray

# If the number is even, divide it by two
# If the number is odd, multiply it by three and add 1
# End program if the current value is 1

number = int (input("enter any positive integer:"))

if number < 0: print ("This is a negative integer. Please enter a positive integer:")

if (number % 2) == 0:
    isEven = True
    print (number / 2, "is an even number")
else:
    isEven = False
    print (number * 3 + 1, "is an odd number")



# I need to get the program to recognise when a negative integer is entered and prompt the user to enter a positive number
# I need the program to end once the current value is 1






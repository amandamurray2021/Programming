# Weekly Task 4
# This program asks the user to input any positive integer
# It outputs the successive values of the following calculation:
# If the number is even, divide it by two
# If the number is odd, multiply it by three and add 1
# End the program if the current value is 1
# Author: Amanda Murray

number = int(input("Please enter a positive integer: "))

while number > 1: # this while loop will run as long as the number is greater than 1
    if (number % 2) == 0: # even number
        number = number // 2
        print (number)
    else:
        (number % 2) == 1 # odd number
        number = 3 * number + 1 # fixed iteration of this line by reviewing Jiang's code
        print (number)

if number <= 0: # this if statement will prevent the user from entering any negative integer 
    print (input("This is not a positive integer. Please enter a positive integer: "))

# Concept for this code influenced by Jiang's and Code Review's sample code (see Works Cited)
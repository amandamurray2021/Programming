# Weekly Task 4
# Author: Amanda Murray

# This program asks the user to input any positive integer
# It outputs the successive values of the following calculation:
# If the number is even, divide it by two
# If the number is odd, multiply it by three and add 1
# End the program if the current value is 1

number = int(input("Please enter a positive integer: "))

while number > 1:
    if (number % 2) == 0:
        number = number // 2
        print (number)
    else:
        (number % 2) == 1
        number = 3 * number + 1
        print (number)
    
if number <= 0:
    print (input("This is not a positive integer. Please enter a positive integer: "))
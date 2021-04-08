# This program is going to make a Fibonacci function.
# It will take in a number and return a list containing the Fibonacci sequence of that many numbers.
# If the user enters in a number less than 0 we should raise a ValueError.
# If the user enters 0 it should return an empty list.
# Author: Amanda Murray

import logging
# logging.basicConfig(level=logging.DEBUG)

# Q1
# You have been asked to make a function called Fibonacci that takes a number and
# returns a list containing a Fibonacci sequence of that many numbers. The function
# will be in a module called myfunctions.py

# Q2
# Define the function Fibonacci that takes in a number
# For the moment let it return an empty list

# def fibonacci (number):
#        return []

def fibonacci (number):
# Q9
# Add the code to throw a ValueError if the number is less than 0. The code
# should begin working now
    if number < 0:
        raise ValueError("number must be > )")

# Q8
# Add the code in case the user enters 0. This will throw an AssertionError
# for not throwing the ValueError when run
    if number == 0: 
        return []

# Q7
# Next, start writing the code for the Fibonacci function. When we run this
# it will throw an AssertionError for 0

    a = 0
    b = 1
    fibonacciSequence = [0]
    # we have one in the list already so number -1 times
    # this is not the most efficient code
    # could have used yield
    for i in range(1, number):
        fibonacciSequence.append(b)
        # this is funky code make a = b and b = a + b
        a , b = b, a + b
    logging.debug("%d: %s", number, fibonacciSequence)

    return fibonacciSequence

# Q3
# Create the section at the bottom of the file that will contain the testing code

# if __name__ == '__main__':
    # tests will go here
    # print ("all good")

# Q4
# Write some test cases that test that the functions called with the parameters
# 7, 11, 0 and 1 all return the correct values

if __name__ == '__main__':
    return7 = [0,1,1,2,3,5,8]
    return11 = [0,1,1,2,3,5,8,13,21,34,55]
    assert fibonacci(7) == return7, "incorrect return for 7"
    assert fibonacci(11) == return11, "incorrect return for 11"
    assert fibonacci(0) == [], "incorrect return value for 0"
    assert fibonacci(1) == [0], "incorrect return value for 1"

# Q5
# This program should return an assertion error if it is run because we have not
# written the body of the function yet

# Q6
# Write the code to test that the function will return a ValueError if a number
# less than 0 is passed in

    try:
        fibonacci(-1)
    except ValueError:
    # we want this exception to be thrown
    # so this is an example where we want to do nothing
        pass
    else:
    # if the exception was not thrown we should throw
    # AssertionError
        assert False, "Fibonacci missing ValueError"
    # or raise AssertionError ("Fibonacci no ValueError")
    print ("all good")


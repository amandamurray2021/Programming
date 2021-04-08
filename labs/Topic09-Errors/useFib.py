# Q10
# Write a program called useFib.py that uses this module to prompt a user for a number and will
# return the list of the Fibonacci sequence (remember to turn off the debug level in the module by
# commenting out the line logging.basicConfig)
# Author: Amanda Murray

import myFunctions

nTimes = int(input("how many:"))
print(myFunctions.Fibonacci(nTimes))
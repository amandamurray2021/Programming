# This program generates 10 random numbers (0-100)
# It prints them out
# Then it prints the top three
# Author: Amanda Murray

# I will use a list to store and manipulate the numbers
import random
howMany = 10
topHowMany = 3
rangeFrom = 0
rangeTo = 100

numbers = []

for i in range(0,10):
    numbers.append(random.randint(rangeFrom, rangeTo))
print ("{} random numbers\t {}".format (howMany, numbers))

topOnes = numbers.copy()
topOnes.sort(reverse = True)
print ("The top {} are \t\t {}".format (topHowMany,topOnes[0:topHowMany]))
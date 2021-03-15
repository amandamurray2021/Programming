# This program puts 10 random numbers into a queue(list)
# It outputs all the values in the queue
# Then it takes the numbers from the queue one at a time
# And prints it and the current numbers still in the queue
# Author: Amanda Murray

import random
queue = []
numberOfNumbers = 10
rangeTo = 100

for n in range (0, numberOfNumbers):
    queue.append(random.randint(0,rangeTo))

print ("queue is {}".format(queue))

while len(queue) != 0:
    currentNumber = queue.pop(0)
    print ("current number is {} and the queue is {} ".format(currentNumber, queue))

print ("the queue is now empty")
# Weekly Task 3
# Author: Amanda Murray

# This program asks the user to input a string
# It outputs every second letter from the string in reverse order

sentence = input("Please enter a sentence: ")
# Example given: The quick brown fox jumps over the lazy dog
print (sentence [::-1][1::2])
# First, we reverse the sentence by slicing the string with a negative index [::-1]
# Next, we address that the first letter in the sentence is counted as 0 and the second letter as 1 by using [1::X] 
# We add the number 2 to the slice [1::2] to make sure we count the second letter in the sentence and every second letter thereafter
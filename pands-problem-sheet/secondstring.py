# Weekly Task 3
# This program asks the user to input a string
# It outputs every second letter from the string in reverse order
# Author: Amanda Murray

sentence = input("Please enter a sentence: ")
print (sentence [::-1][::2])
# Example given: The quick brown fox jumps over the lazy dog.
# We reverse the sentence by slicing the string with a negative index [::-1]
# We add the number 2 as a new slice [::2] to count every second letter from the reverse order
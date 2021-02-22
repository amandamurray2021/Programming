# Assessment 2
# secondstring.py
# Author: Amanda Murray

# This program asks the user to input a string and outputs every second letter in reverse order

sentence = ("The quick brown fox jumps over the lazy dog")
print (sentence [::-1])
reverseSentence = ("god yzal eht revo spmuj xof nworb kciuq ehT")
print (len(sentence))

primes = range (0, 44)
for number in range (0, 44):
    isPrime= True
    for divisor in primes:
        if (number % divisor == 0):
            isPrime = False
            break
    if isPrime:
        print (primes)
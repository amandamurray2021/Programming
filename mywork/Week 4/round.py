# This program rounds a student's decimal point percentage mark 
# and then prints out the corresponding grade
# Author: Amanda Murray

percentage = float(input("Enter the percentage: "))

if percentage < 39.4: # 39.4 or less
    print ("Fail")
elif percentage <= 49.4: # between 39.5 to 49.4
    print ("Pass")
elif percentage <= 59.4: # between 49.5 to 59.4
    print ("Merit 2")
elif percentage <= 69.4: # between 59.5 to 69.4
    print ("Merit 1")
else: # from 69.5 to 100
    print ("Distinction")
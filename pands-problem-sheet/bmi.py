# bmi.py
# This program calculates a person's Body Mass Index (BMI)
# Inputs are the person's height in cm and weight in kg
# Output is the weight divided by their height in m²

# Height = 180cm
# Weight = 65kg

# Author: Amanda Murray

# first we need to convert 180cm to 1.8m²

x = int ('180')
y = int ('100')
answer = x / y
print ('{} divided by {} equals to {}'.format (x, y, answer))

# next, we need to calculate what 1.8m² is 
a = float ('1.8')
result = a * a
print ('{} multiplied by {} equals to {}'.format (a, a, result))

# finally we can calculate the bmi
weight = int ('65')
height = float ('3.24')
bmi = 20.06
print ('{} divided by {} is {}'.format(weight, height, bmi))
print ('Your BMI is 20.06')
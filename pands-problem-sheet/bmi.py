# Assessment 1
# bmi.py
# Author: Amanda Murray

# This program calculates a person's Body Mass Index (BMI)
# Inputs are the person's height in cm and weight in kg:

# Height = 180cm
# Weight = 65kg

# The output will be their weight divided by their height in m² (BMI):
# BMI = 20.06

# First we need to convert 180cm to m²
# We are dividing by 100 as there are 100cm in 1m

cm = 180
m = 100
answer = cm / m
print ('{} divided by {} equals to {}'.format (cm, m, answer))
# 180cm / 100 = 1.8m²

# Now that we have converted cm to m², we have 2 ways of finding the person's BMI:
# 1
# We multiply 1.8 * 1.8 to calculate 1.8m²:
height = 1.8
answer = 1.8 * 1.8
print ('{} multiplied by {} equals to {}'.format (height, height, answer))
# 1.8 * 1.8 = 3.24

# Then we calculate their BMI:
weight = 65
height = 3.24
answer = weight / height
print ('{} divided by {} is {}'.format (weight, height, answer))
# 65 / 3.24 = 20.061728395061728

# 2 
# We enter the multiplication into the program when calculating their BMI:
weight = 65
height = (1.8 * 1.8)
answer = weight / height
print ('{} divided by {} is {}'.format (weight, height, answer))
# 65 / 3.24 = 20.061728395061728

# Once we have the BMI as a float figure, we round the number to two decimal places:
bmi = 20.061728395061728
bmi_r = round (bmi, 2)
print ('Your BMI is: ' + str (bmi_r)) # Float is converted to str so the statement can be output as a str
# 'Your BMI is 20.06'
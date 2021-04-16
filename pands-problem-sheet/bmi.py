# Weekly Task 2
# Author: Amanda Murray

# This program calculates a person's Body Mass Index (BMI)
# The inputs are the person's height in centimetres and weight in kilograms
# The output will be their weight divided by their height in metres squared (BMI)

cm = int(input ('Please enter your height (in cm): '))
kg = int(input ('Please enter your weight (in kg): '))

# First, we need to convert centimetres to metres squared
# We are dividing by 100 as there are 100 centimetres in 1 metre
metres = cm / 100
print ('{} divided by 100 equals to {}'.format (cm, metres))

# Next, we multiply metres by metres to calculate m²:
metressquared = metres * metres
print ('{} multiplied by {} equals to {}'.format (metres, metres, metressquared))

# Finally, we calculate the BMI by dividing their weight by their height in m²
bmi = kg / metressquared
print ('{} divided by {} equals to {:.2f}'.format (kg, metressquared, bmi))
print ('Your BMI is {:.2f}'.format (bmi))
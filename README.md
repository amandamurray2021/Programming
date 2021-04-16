# Weekly Tasks

This is a description of the weekly tasks that I have completed as part of the Programming and Scripting module for the Higher Diploma in Data Analytics.

## Table of Contents
### bmi.py
This program accepts an integer input of a person's height in centimetres and their weight in kilograms. 

It converts centimetres to metres squared by dividing the input in centimetres by 100 (as there are 100 centimetres in a metre). 

It multiplies the value in metres by itself to calculate metres squared.

It outputs the person's BMI by dividing their weight in kilograms by their height in metres squared.

It displays their BMI rounded to 2 decimal places.

##### Works cited
“Python Comments.” W3Schools, Refsnes Data, www.w3schools.com/python/python_comments.asp. Accessed 12 Apr. 2021.

“Python Data Types.” W3Schools, Refsnes Data, www.w3schools.com/python/python_datatypes.asp. Accessed 12 Apr. 2021.

“Python String Formatting.” W3Schools, Refsnes Data, www.w3schools.com/python/python_string_formatting.asp. Accessed 12 Apr. 2021.

“Python User Input.” W3Schools, Refsnes Data, www.w3schools.com/python/python_user_input.asp. Accessed 12 Apr. 2021.

Sweigart, Al. Automate the Boring Stuff with Python: Practical Programming for Total Beginners. 2nd ed., No Starch Press Inc., 245 8th Street, San Francisco, CA 94103, 2015, http://files.urpdfs.com/automate-the-boring-stuff-with-python.pdf

### secondstring.py
This program asks the user to input a string.

The string is then reversed by slicing the string (::-1).

Next, a value of (1::2) is used to address that the first letter in the sentence is counted as 0 and the second letter as 1.

This will display the second letter in the sentence in reverse order and every second letter thereafter.

#### Works cited
“Python User Input.” W3Schools, Refsnes Data, www.w3schools.com/python/python_user_input.asp. Accessed 12 Apr. 2021.

“Python Slicing Strings.” W3Schools, Refsnes Data, www.w3schools.com/python/python_strings_slicing.asp. Accessed 13 Apr. 2021.

#### collatz.py
This program asks the user to input any positive integer.

It outputs the successive values of the following calculation:
If the number is even, divide it by 2.
If the number is odd, multiply it by 3 and add 1.
End the program if the current value is 1.

This program accepts an integer input of the positive integer.

It uses a while loop to make sure that the program will only continue running if the number is greater than 1.

It implements an if statement so that if the inputted integer divided by 2 has a remainder of 0 (making it an even number) that the integer will be divided by 2 and printed.

It also implements an else statement that if the inputted integer divided by 2 has a remainder of 1 (making it an odd number) that the integer will be multiplied by 3 and plus 1. 

Finally, it has another if statement at the end so that if the user enters a value less than or equal to 0, the program will tell them that the inputted integer is not a positive integer and prompts them to enter a positive integer again.

#### Works cited
“Python User Input.” W3Schools, Refsnes Data, www.w3schools.com/python/python_user_input.asp. Accessed 12 Apr. 2021.

“Python Conditions.” W3Schools, Refsnes Data, www.w3schools.com/python/python_conditions.asp. Accessed 14 Apr. 2021.

“Python For Loops.” W3Schools, Refsnes Data, www.w3schools.com/python/python_for_loops.asp. Accessed 14 Apr. 2021.

“Python While Loops.” W3Schools, Refsnes Data, www.w3schools.com/python/python_while_loops.asp. Accessed 14 Apr. 2021.

Sweigart, Al. Automate the Boring Stuff with Python: Practical Programming for Total Beginners. 2nd ed., No Starch Press Inc., 245 8th Street, San Francisco, CA 94103, 2015, http://files.urpdfs.com/automate-the-boring-stuff-with-python.pdf

“Python - The Collatz Sequence.” Code Review Stack Exchange, Stack Exchange Inc., codereview.stackexchange.com/questions/229270/python-the-collatz-sequence. Accessed 14 Apr. 2021.

Jiang, Lin. “The Collatz Sequence in Python - The Art of Python.” Medium, 10 Mar. 2021, medium.com/the-art-of-python/the-collatz-sequence-in-python-eb7e1f1b4f9e. Accessed 14 Apr. 2021.

### weekday.py
This program outputs whether or not today is a weekday.

First, we import the datetime module so that it can give functionality to check if today's date is a weekday or a weekend.

The code is not running at the moment.

In order to have the code run successfully, we must have the program use the datetime.date.today() and datetime.weekday() functions to determine the date and the day.

#### Works cited
“Python Dates.” W3Schools, Refsnes Data, www.w3schools.com/python/python_datetime.asp. Accessed 15 Apr. 2021.

“Python Lists.” W3Schools, Refsnes Data, www.w3schools.com/python/python_lists.asp. Accessed 14 Apr. 2021.

Sturtz, John. “Lists and Tuples in Python.” Real Python, realpython.com/python-lists-tuples. Accessed 14 Apr. 2021.

Sweigart, Al. Automate the Boring Stuff with Python: Practical Programming for Total Beginners. 2nd ed., No Starch Press Inc., 245 8th Street, San Francisco, CA 94103, 2015, http://files.urpdfs.com/automate-the-boring-stuff-with-python.pdf

#### squareroot.py
This program accepts an input of a positive floating point number.

It outputs an approximation of it's square root using a created function called 'sqrt' to do so.

It does not use the built-in functions x**.5 or math.sqrt(x).

It is based on the Newton method of estimating square roots.

Although I did find some references on this topic, I was unable to find a method of performing this within my coding capabilities.

#### Works cited
Kong, Qingkai, et al. Python Programming and Numerical Methods: A Guide for Engineers and Scientists. 1st ed., Cambridge, Massachusetts, Academic Press, 2020, pythonnumericalmethods.berkeley.edu/notebooks/chapter19.04-Newton-Raphson-Method.html.

“Python Dates.” W3Schools, Refsnes Data, www.w3schools.com/python/python_datetime.asp. Accessed 15 Apr. 2021.

“Python Lists.” W3Schools, Refsnes Data, www.w3schools.com/python/python_lists.asp. Accessed 14 Apr. 2021.

Sturtz, John. “Lists and Tuples in Python.” Real Python, realpython.com/python-lists-tuples. Accessed 14 Apr. 2021.

VanderPlas, Jake. A Whirlwind Tour of Python. 1st ed., 1005 Gravenstein Highway North, Sebastopol, CA 95472, O’Reilly Media, Inc, 2016, jakevdp.github.io/WhirlwindTourOfPython/06-built-in-data-structures.html.

### es.py
This program reads in a text file. It takes the filename from an argument on the command line. 

The function readnumber reads in three arguments: the filename, the number and the characters (uppercase and lowercase e's).

Using a for loop to find a character in the file, an if statement advises that if the character is an uppercase E it should be added to the count which is set as 0. It also uses 
an elif statement to include all lowercase e's to the count.

Finally, it returns the count and prints out the amount of e's in the text.

#### Works cited
GeeksforGeeks. “Count the Number of Times a Letter Appears in a Text File in Python.” GeeksforGeeks, 25 Nov. 2020, www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python. Accessed 15 Apr. 2021.

“Python File Open.” W3Schools, Refsnes Data, www.w3schools.com/python/python_file_handling.asp. Accessed 15 Apr. 2021.

“Python File Write.” W3Schools, Refsnes Data, www.w3schools.com/python/python_file_write.asp. Accessed 15 Apr. 2021.

“Python List Count() Method.” W3Schools, Refsnes Data, www.w3schools.com/python/ref_list_count.asp. Accessed 15 Apr. 2021.

Singh, Deepak. “Python Count Alphabets in Text File.” Pyforschool, www.pyforschool.com/assignment/file-handling/count-occurance-of-alphabet-text-file.html. Accessed 15 Apr. 2021.

“The Project Gutenberg EBook of Moby-Dick; or The Whale, by Herman Melville.” Project Gutenberg, Daniel Lazarus, Jonesey, and David Widger, June 2001, gutenberg.org/files/2701/2701-0.txt.

“UnicodeDecodeError: ‘charmap’ Codec Can’t Decode Byte 0x9d in Position X: Character Maps To.” Stack Overflow, Stack Exchange Inc., stackoverflow.com/questions/49640513/unicodedecodeerror-charmap-codec-cant-decode-byte-0x9d-in-position-x-charac. Accessed 15 Apr. 2021.

Sweigart, Al. Automate the Boring Stuff with Python: Practical Programming for Total Beginners. 2nd ed., No Starch Press Inc., 245 8th Street, San Francisco, CA 94103, 2015, http://files.urpdfs.com/automate-the-boring-stuff-with-python.pdf

### plottask.py
This program displays a plot of the functions: f(x) = x, g(x) = x², h(x) = x³ in the range (0,4) on one set of axes.

First, I imported matplotlib.pyplot which will allow for visualisation of the plotting of the graph.

Next, I imported NumPy which is needed for working with arrays.

I have used a dictionary description describing the font, color and size of the title, xlabel and ylabel.

I have plotted x in the color pink with markers for the points.

I have plotted g in the color purple with markers for the points.

I have plotted h in the color orange with markers for the points.

I have saved the graph as a .png file for viewing.

#### Works cited
“Matplotlib Labels and Title.” W3Schools, Refsnes Data, www.w3schools.com/python/matplotlib_labels.asp. Accessed 16 Apr. 2021.

“Matplotlib Markers.” W3Schools, Refsnes Data, www.w3schools.com/python/matplotlib_markers.asp. Accessed 16 Apr. 2021.

“Matplotlib Plotting.” W3Schools, Refsnes Data, www.w3schools.com/python/matplotlib_plotting.asp. Accessed 16 Apr. 2021.

“Matplotlib Pyplot.” W3Schools, Refsnes Data, www.w3schools.com/python/matplotlib_pyplot.asp. Accessed 16 Apr. 2021.

“Matplotlib (Pyplot) Savefig Outputs Blank Image.” Stack Overflow, Stack Exchange Inc., stackoverflow.com/questions/9012487/matplotlib-pyplot-savefig-outputs-blank-image. Accessed 16 Apr. 2021.

“NumPy Getting Started.” W3Schools, Refsnes Data, www.w3schools.com/python/numpy/numpy_getting_started.asp. Accessed 16 Apr. 2021.

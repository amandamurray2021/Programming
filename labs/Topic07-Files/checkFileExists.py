# Q2(d)
# This program creates an OS "init" program that initialises count.txt instead.
# Write some code to check if the file exists.
# You will need to import os.path and use the isfile() function.
# Author: Amanda Murray

import os.path

filename = "count.txt"
isfile = 'Users\amand\Desktop\GMIT\Programming'
if not os.path.isfile(filename):
    print ("File does not exist")
else:
    print ("This file already exists")
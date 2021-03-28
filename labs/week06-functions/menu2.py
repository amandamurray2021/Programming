# Q3
# This program uses the function from student.py.
# It keeps displaying the menu until the user picks Q.
# If the user chooses a, then call a function called doAdd ().
# If the user chooses v, then call a function called doView ().

def displayMenu ():
    print ("What would you like to do?")
    print ("\t (a) Add new student")
    print ("\t (v) View students")
    print ("\t (q) Quit")
    choice = input ("Type one letter (a/v/q):").strip ()

    return choice

def doAdd ():
    print ("in adding")
def doView ():
    print ("in viewing")

# main program
choice = displayMenu ()
while (choice != 'q'):
    if choice == 'a':
        doAdd ()
    elif choice == 'v':
        doView ()
    elif choice != 'q':
        print ("\n\n please select either a, v or q")
    choice = displayMenu ()
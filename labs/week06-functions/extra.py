# Extra
# This program shows that variables can be of type function.
# This means that lists, tuples and dicts can have variables of type function in them.
# Author: Amanda Murray

def fun1 ():
    print ("this is fun1")
def fun2 ():
    print ("this is fun2")

whichFun = fun1
whichFun ()
whichFun = fun2
whichFun ()
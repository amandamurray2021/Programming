# Q4
# This function will read in a dict object from a JSON file.
# Author: Amanda Murray

import json
filename = "testdict.json"

def readDict():
    # this will throw an error if the file does not exist
    # it should really just return an empty dict
    # we can do this later
    with open (filename) as f:
        return json.load(f)

# test the function
somedict = readDict ()
print (somedict)
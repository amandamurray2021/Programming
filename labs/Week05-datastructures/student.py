# Q4
# This program stores a student name and a list of her courses and grades in a dict
# The program should print out her data
# The number of courses she has could change
# Author: Amanda Murray

student = {
    "name":"Mary",
    "modules": [
        {
            "coursename":"Programming",
            "grade": 45
        },
        {
            "coursename":"History",
            "grade": 99
        }
  ]
}
print ("Student: {}".format(student["name"]))
for module in student ["modules"]:
    print ("\t {} \t: {}".format(module["coursename"], module["grade"]))
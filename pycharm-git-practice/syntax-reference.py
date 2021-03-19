"""
Theses are some changes made on the pycharm branch
"""


# It's print
print("Text")

integer = 10
float_number = 10.0

# Lists are mutable and square brackets
a_list = [1, 2, 3]

# Tuples are immutable and regular brackets
a_tuple = (1, 2, 3)


# How to do a function
def a_function(an_argument):
    print("I am a function, I have been given: " + an_argument)
    return None


# For loops
for each_item in a_list:
    # Remember, things are 0-indexed
    print(a_list[each_item - 1] ** 2)

a_variable = "I am a variable"
a_function(a_variable)
a_condition = True

# While loops
while (a_condition == True):
    print("My condition is: " + str(a_condition))
    a_condition = False

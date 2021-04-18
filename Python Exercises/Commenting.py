# different ways to comment

# this is my code

"""
This is my note
and this is still my note
and this again is still my note.
"""

##This is a line of code is commented with ALT + 3, uncommented with ALT + 4


def printMe():
    """This is my docstring
    """

    print("Me there")

print(printMe.__doc__)  # print out the docstring

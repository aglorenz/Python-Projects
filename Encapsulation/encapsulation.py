#
# Python Ver: 3.9.5
#
# Author:       Andrew Lorenz
#
# Purpose:      Create a class that uses encapsulation.  The class should use:
#               1) a private attribute or function
#               2) a protected attribute or function
#
#               Create an object that uses the protected and private attribute or function
#
# Tested OS:    This code was written and tested to work with Windows 10.


# 
class Student:
    """Class to demonstrate encapsulation"""
    
    def __init__(self, name, phone):
        # protected vars are prefixed with _
        self._fname = name
        self._phone = phone
        self.__highSchool = "Cordova" # private class attribute prefixed with __
        
    # Private attributes must be accessed with get/set functions else you get an error
    def getHighSchool(self):        # Gets the private attribute value
        return self.__highSchool

    def setHighSchool(self, highSchool): # Set's the value of the private attribute
        self.__highSchool = highSchool

if __name__ == "__main__":
    student1 = Student("Andy","555-555-5555")
    print("Student Name: {}\nPhone: {}\n"
          .format(student1._fname,student1._phone))

    # print(student1.__highSchool) # this will fail.  Must use get/set functions to access
    
    print("{}'s high school is {}".format(student1._fname, student1.getHighSchool()))
    print("Updating {}'s high school".format(student1._fname))
    student1.setHighSchool("Cactus")
    print("{}'s high school is now {}".format(student1._fname, student1.getHighSchool()))

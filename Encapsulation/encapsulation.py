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
    """
    Sample Student Class to demonstrate encapsulation

    ...  Additional explanation goes here ...

    Attributes
    ----------
    _name : str
        The name of the student (protected)
    _phone : str
        The phone number of the student (protected)
    __highSchool : str
        The name of the student's current high school (private, initialized as "Cordova")

    Methods
    -------
    getHighSchool()
        Gets the private attribute __highSchool

    setHighSchool()
        Sets the private attribute __highSchool
    """
    
    def __init__(self, name, phone, highschool):
        '''
        Initialize the class attributes

        Parameters
        ----------
        name : str
            The name of the student
        phone : str
            The phone number of the student
        '''
        
        # protected vars are prefixed with _
        self._fname = name
        self._phone = phone
        self.__highSchool = highschool # private class attribute prefixed with __
        
    # Private attributes must be accessed with get/set functions else you get an error
    # Gets the private attribute value
    def getHighSchool(self):
        ''' Returns the value of the private attribute, __highschool'''
        return self.__highSchool

    # Set's the value of the private attribute
    def setHighSchool(self, highSchool): 
        ''' Sets the value of the private attribute, __highschool

        Parameters
        ----------
        highSchool : str
            The name of the student's new high school

        Raises
        -------
        none
        '''
        
        self.__highSchool = highSchool

if __name__ == "__main__":
    student1 = Student("Andy","555-555-5555", "Lincoln")  # you can initialize a private attribute
    print("Student Name: {}\nPhone: {}\n"
          .format(student1._fname,student1._phone))

    #print(student1.__highSchool) # this will fail.  Must use get/set functions to access the attribute
    
    print("{}'s high school is {}".format(student1._fname, student1.getHighSchool()))
    print("Updating {}'s high school".format(student1._fname))
    student1.setHighSchool("Laurelwood")
    print("{}'s high school is now {}".format(student1._fname, student1.getHighSchool()))

#
# Python:   3.9.4
#
# Author:   Andy Lorenz
#
# Purpose:  The Tech Academy - Python Course, Creatin our first program together.
#           Demonstrating how to pass variables from function to function
#           while producting a functional game.
#
#           Remember, function_name(variable) _means that we pass in the variable.
#           return variable _means that we are returning the variable back
#           to the calling function.


def start():
    f_name = "Sarah"
    l_name = "Connor"
    age = 28
    gender = "Female"
    get_info(f_name, l_name, age, gender)
    #print("Hello {}!".format(get_info()))  # print the result of get_name()


def get_info(f_name, l_name, age, gender):
    print("My name is {} {}. I am a {} year old {}.".format(f_name, l_name, age, gender))
    #name = input("What is your name? ")
    #return name






if __name__ == "__main__":
    start()

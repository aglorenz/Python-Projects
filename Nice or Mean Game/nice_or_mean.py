#
# Python:   3.9.4
#
# Author:   Andy Lorenz
#
# Purpose:  The Tech Academy - Python Course, Creating our first program together.
#           Demonstrating how to pass variables from function to function
#           while producing a functional game.
#
#           Remember, function_name(variable) _means that we pass in the variable.
#           return variable _means that we are returning the variable back
#           to the calling function.


from playsound import playsound

# initialize the game vars at game start
def start(nice=0, mean=0, name=""):
    # get user's name
    name = describe_game(name)
    nice, mean, name = nice_mean(nice,mean,name)

def describe_game(name):
    """
        Check if this is a new game or not,
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game
    """
    # meaning, if we do not already have this user's name,
    # then they are a new player and we need to get their name
    if name != "":
        print("\Thank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you  will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name                    
                             
# This is the main loop in the game.  The loop checks for valid answer and adds 1 to either nice or mean
def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation.  Will you be nice\nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice += 1
            stop = False
        if pick == "m":
            print ("\nThe stranger glares at you  \nmenacingly and storms off...")
            mean += 1
            stop = False
    score(nice,mean,name)  # pass the 3 vars to the score() function    

# Display the current score
def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))

# Determine if the player wins or loses.
# If mean > 2, then call  the lose function, if win > 2, then call the win function.  Otherwise, call nice_mean() again.
def score(nice,mean,name):
    # score function is being passed the values stored within the 3 vars
    if nice > 2: # if conditions is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2: # if condition is valid, call losew function passing in the variables so it can usew them
        lose(nice,mean,name)
    else:       # else, call nice_mean function passing in the vvariables so iti can usew them
        nice_mean(nice,mean,name)

# print message and sound when player wins.
def win(nice,mean,name):
    #Substitue the {} wildcars with our var values
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    # call again function and pass in our variables
    playsound('homer_snicker.wav')
    again(nice,mean,name)

# print message and play sound when player loses
def lose(nice,mean,name):
    #Substitue the {} wildcars with our var values
    print("\nAhhh too bad, game over! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    playsound('doh.wav')
    # call again function and pass in our variables
    again(nice,mean,name)
    
# ask the user if they want to play again.  If so, reset the game.
def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>>").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")

# reset the game if user wants to play again
def reset(nice,mean,name):
    nice = 0
    mean = 0
    #Notice, I do not reset the name variable as that same user has selecte to play again
    start(nice,mean,name)
                


if __name__ == "__main__":
    start()

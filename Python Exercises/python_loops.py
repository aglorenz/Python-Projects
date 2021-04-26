

mySentence = 'loves the color'

color_list = ['red','blue','pink','teal','black']

def color_function(name):
    lst = []
    for i in color_list:
        msg = '{} {} {}'.format(name, mySentence, i)
        lst.append(msg)
    return lst

def get_name():
    #go = True
    name = input('What is your name : ')
    while name == '':
        #name = input('What is your name : ')
        #if name == '':
        print ("You need to provide you name")
        #    print("Sally, you may not use this software")
        #else:
        #    go = False
        name = input('What is your name : ')
    lst = color_function(name)
    for x in lst:
        print(x)

get_name()


def myFun(*args):
    for arg in args:
        print(arg)

def myFun1(**kwargs):
    print("kwargs", kwargs)
    

if __name__ == "__main__":
    myFun('This is an example of args','string','and then an ingeger',5)

    myFun1(first = '1', second = '2', third = '3')
    
# some programmers use **args instead of **kwargs both are valid

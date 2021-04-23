

def getInfo():
    var1 = input("Please provide the first numeric value: ")
    var2 = input("Please provide the second numeric value: ")
    return var1, var2

def compute():
    go = True
    while go:
        input1, input2 = getInfo()
        try:
            mySum = int(input1) + int(input2)
            go = False
        except ValueError as e:
            # e contains the system error message
            print("{}: \nPlease provide a numeric value!".format(e))
        except:
            print("{}: \nOops, you provided invalid input, program iwll close now!".format(e))
    print("{} + {} = {}".format(input1, input2, mySum))

        
##    finally:
##        print("Moving on...")
        

if __name__ == "__main__":
    compute()

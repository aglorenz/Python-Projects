#print(dir(str))
#print(help(str))
#print (help(os))

import os
#print (os.getcwd())

def writeData():
    data = '\nHello world!'
    with open('test.txt','a') as f:
        f.write(data)
        #f.close() # not needed since we are using 'with'
        
# This function will read the whole file and store it in variable called data
def openFile():
    with open('test.txt','r') as f:
        f = open('test.txt','r')
        data = f.read()
        print(data)
        #The with keyword is syntactic sugar and takes place of try/catch/finally and closing of the file
        #f.close()  close is not needed because we are uring the with keyword

if __name__ == "__main__": 
    writeData()
    openFile()
    

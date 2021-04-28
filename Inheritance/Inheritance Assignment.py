#
# Create two classes that inherit from another class
# Ensure each child has at least two of their own attributes.
# Add comments throughout, explaining your code.
#

# Base class 
class User:
    #Define the attributes of the class
    name = "No Name Provided"
    email = ""
    password = "1234abcd"
    account = 0

    #Define the methods of the class
    def login(self):
        entry_email = input("Enter your email: ")
        entry_password  = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("You are not authorized for this page.")

    # Dunder method allows us to pass in parameters when instantiating the class
    # We don't call it directly.  It gets called automatically when we pass in the
    # parms on instantiation.
    def __init__(self, name, email, password, account):
        self.name = name
        self.email = email
        self.password = password
        self.account = account

# Employee class inherits everything from the User class and adds its own attributes
class Employee(User):
    base_pay = 11.00
    department = 'General'

# Customer class inherits everything from the User class and adds its own attributes
class Customer(User):
    mailing_address = ' '
    mail_list = True



if __name__ == "__main__":
        
    #Outside of the class you create an instance of the User class
    new_user = User("Andy", "andy@gmail.com", "p@ssw0rd", 1234)

    #Call the login method using the new object
    new_user.login()


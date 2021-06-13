from abc import ABC, abstractmethod

class Car(ABC): # ABC = ABstract Class, imported from abc
    def pay_slip(self, amount):
        print("Your purchase amount: ", amount)

    # This is an abstract method.  It is telling us to pass in an argument, but we won't tell
    # you what kind of data it will be.
    @abstractmethod  # imported from abc
    def payment(self, amount):
        pass

# Child Class must define the implementation of its parent's abstract method
class DebitCardPayment(Car):
    # Here we implement the payment method from the parent Car class
    def payment(self, amount):
        print("Your purchase amount of {} exceeded your $100 limit ".format(amount))

obj = DebitCardPayment()
obj.pay_slip("$400")
obj.paysment("$400")
             
# Output
# Your purchase amount:  $400
# Your purchase amount of $400 exceeded your $100 limit 

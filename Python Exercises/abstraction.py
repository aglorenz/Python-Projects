from abc import ABC, abstractmethod

class Car(ABC):
    def pay_slip(self, amount):
        print("Your purchase amount: ", amount)

    # this function is telling us to pass in an argument, but we won't tell
    # you how or what kind of data it will be.
    @abstractmethod
    def payment(self, amount):
        pass

class DebitCardPayment(Car):
    # here we implement the payment function from it's parent car class
    def payment(self, amount):
        print("Your purchase amount of {} exceeded your $100 limit ".format(amount))

obj = DebitCardPayment()
obj.pay_slip("$400")
obj.payment("$400")
             
# Output
# Your purchase amount:  $400
# Your purchase amount of $400 exceeded your $100 limit 

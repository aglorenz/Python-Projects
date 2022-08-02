from abc import ABC, abstractmethod

class Food(ABC): # ABC = ABstract Class, imported from abc
    def dish(self, meal):
        print("\nThe dish you've chosen to prepare is: ", meal)

    # This is an abstract method.  It is telling us to pass in an argument, but we won't tell
    # not what kind of data it will be.
    @abstractmethod  # imported from abc
    def preparation(self, meal):
        pass

# This child class must define the implementation of its parent's abstract method
class HomeCooked(Food):
    # Here we implement the payment method from the parent Car class
    def preparation(self, meal):
        print("Your meal of {} will take 3 hours to prepare in the kitchen".format(meal))

class CampCooked(Food):
    # Here we implement the payment method from the parent Car class
    def preparation(self, meal):
        print("Your meal of {} will take 10 minutes to prepare over a fire".format(meal))

home_meal = HomeCooked()
home_meal.dish("lasagne")
home_meal.preparation("lasagne")

camp_meal = CampCooked()
camp_meal.dish("smores")
camp_meal.preparation("smores")
             
# Output
# The dish you've chosen to prepare is:  lasagne
# Your meal of lasagne will take 3 hours to prepare in the kitchen
#
# The dish you've chosen to prepare is:  smores
# Your meal of smores will take 10 minutes to prepare over a fire

class vehicle:
  def __init__(self,color):
    self.color=color
  def start(self):
    print("Starting engine")
  def showcolor(self):
    # These both produce the same output  
    print(f"I am {self.color}")
    print("I am {}".format(self.color))

car=vehicle('black')
car.start()
car.showcolor()

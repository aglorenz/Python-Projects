
import ourModule
from datetime import datetime

if __name__ == "__main__":
  myResults = ourModule.getNumbers(5,9)
  print(myResults)
  myDate = datetime.now()
  print("The current date is {}".format(myDate))

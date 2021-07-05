from datetime import *
import pytz

fmt = '%H:%M:%S %Z%z'
d = datetime.now()

hqTimezone = pytz.timezone('US/Pacific')
hqTime = d.astimezone(hqTimezone)
print(hqTime.hour)
convHqTime = hqTime.strftime(fmt)
print("The time in Portland is " + convHqTime)
if (hqTime.hour > 17 or hqTime.hour < 9):
    print("We are closed.")
else:
    print("We are open!")
    
nyTimezone = pytz.timezone('US/Eastern')
nyTime = d.astimezone(nyTimezone)
convNyTime = nyTime.strftime(fmt)
print("The time in New York is " + convNyTime)
if (nyTime.hour > 17 or nyTime.hour < 9):
    print("We are closed.")
else:
    print("We are open!")
    
londonTimezone = pytz.timezone('Europe/London')
londonTime = d.astimezone(londonTimezone)
convLondonTime = londonTime.strftime(fmt)
print("The time in London is " + convLondonTime)
if (londonTime.hour > 17 or londonTime.hour < 9):
    print("We are closed.")
else:
    print("We are open!")

#import datetime
# help from https://realpython.com/python-datetime/
# help from https://www.w3schools.com/python/python_datetime.asp
# importing only the functions we need
from datetime import datetime, timedelta
import pytz
from pytz import timezone

# list all available timezonesm we want PDX, NYC, and London
print(pytz.all_timezones)  # squeezed into 136 lines output

# time format is used by strftime method in datetime module
time_fmt = '%H:%M:%S %Z%z'  # Ex: 19:34:13 PDT-0700

# set timezones objects
portland = pytz.timezone('US/Pacific')
new_york = pytz.timezone('US/Eastern')
london = pytz.timezone('Europe/London')  # or you can use "GB"
print (type(portland)) # <class 'pytz.tzfile.US/Pacific'>

print(portland.zone)
print(new_york.zone)
print(london.zone)

pdx_dt = portland.localize(datetime.now()) # looks like 19:38:55 PDT-0700
pdxx_dt = datetime.now() # looks like 19:38:55
print (pdxx_dt.strftime(time_fmt))
print ("\nThe current time in Portland is {}".format(pdx_dt.strftime(time_fmt)))
if pdx_dt.hour > 8 and pdx_dt.hour < 17 :
    print("Portland is open")
else:
    print("Portland is closed")

nyc_dt = pdx_dt.astimezone(new_york)
print ("\nThe current time in New York is {}".format(nyc_dt.strftime(time_fmt)))
if nyc_dt.hour > 8 and nyc_dt.hour < 17 :
    print("New York is open")
else:
    print("New York is closed")


london_dt = pdx_dt.astimezone(london)
print ("\nThe current time in London is {}".format(london_dt.strftime(time_fmt)))
if london_dt.hour > 8 and london_dt.hour < 17 :
    print("London is open")
else:
    print("London is closed")

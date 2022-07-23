import selenium
from selenium import webdriver
import time
import urllib
import urllib.request, urllib.error

# How to install Chrome driver
# https://stackoverflow.com/questions/42478591/python-selenium-chrome-webdriver  use below link to download. old site deprecated
# https://sites.google.com/chromium.org/driver/

lms_tab_1 = "https://www.learncodinganywhere.com/Instructor/Feedback/AssignmentIndex?pageNumber=1&tabNumber=1"
lms_tab_2 = "https://www.learncodinganywhere.com/Instructor/Feedback/AssignmentIndex?pageNumber=1&tabNumber=2"
refresh_rate = input("Enter refresh rate in seconds > ")
refresh_rate = int(refresh_rate)
browser = webdriver.Chrome(executable_path=r"C:\Users\Andy\Source\Repos\Python-Projects\chromedriver.exe")

browser.get(lms_tab_2)

##print(type(refresh_rate))

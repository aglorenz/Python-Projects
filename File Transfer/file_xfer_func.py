import shutil
import os, time
from datetime import datetime, timedelta

#import tkinter as tk
#from tkinter import Frame
from tkinter import filedialog as fd

import file_xfer_main
import file_xfer_gui

def center_window(self, w, h): # pass in the tkinter frame (master) reference and the v and h
    '''Center the application window on the user's screen'''
    
    # get User's screen width and height
    screen_width = self.master.winfo_screenwidth() # get user's width and height
    screen_height = self.master.winfo_screenheight() # and height
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    center_geo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return center_geo

def get_folder(self, entry_box):
    '''Browse for a file folder and store result in given Entry widget '''
    entry_box.delete(0,'end')
    src_folder = fd.askdirectory()
    entry_box.insert(0,src_folder)

##    self.txt_source.delete(0,'end')
##    src_folder = fd.askdirectory()
##    self.txt_source.insert(0,src_folder)

def xfer_files(self):

    # get the source path of the files
    source = self.txt_source.get()
    print(source)

    # get the destination path of the files
    destination = self.txt_dest.get()
    print(destination)

    # get list of files from source
    files = os.listdir(source)

    # in epoch format
    one_day_ago = (datetime.now()-timedelta(hours=24)).timestamp()

    one_day_as_seconds = 86400 # seconds in a day

    # Move files to their new destination if then are less than 24 hours old.
    for file_name in files:
        print(source)
        print(file_name)
        file_path = source + '/' + file_name
        print(file_path)
        mod_date_in_sec = os.path.getmtime(file_path)
        mod_date = time.ctime(mod_date_in_sec)
        
        print('File: {} \nMDate: {} \nMDate in Sec: {}\n'
              .format(file_path, mod_date, mod_date_in_sec))

        # if file mod date is less than one day ago, then move file to 2nd folder
        if(mod_date_in_sec > one_day_ago):
            #shutil.move(file_path, destination)
            print('Moved\n')
        else:
            print('Not Moved\n')

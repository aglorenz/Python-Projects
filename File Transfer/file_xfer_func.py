#
# Python Ver:   3.9.5
#
# Author:       Andrew Lorenz
#
# Tested OS:  This code was written and tested to work with Windows 10.

'''
Module with functions to facilitate the file transfer application

Functions:

    center_window(self, w, h)
    get_folder(entry_box)
    xfer_files(source, destination)
    
'''

import shutil
import os, time
from datetime import datetime, timedelta

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

import file_xfer_main

def center_window(self, w, h):
    '''Center the application window on the user's screen

    Parameters
    ----------
    self : Frame
        The tkinter Frame to center in the user's window
    w : int
        The width of the tkinter Frame
    h : int
        The height of the tkinter Frame

    Returns
    -------
        None
    '''
    
    # get User's screen width and height
    screen_width = self.master.winfo_screenwidth() # get user's screen width
    screen_height = self.master.winfo_screenheight() # and height
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))

def get_folder(entry_box):
    '''Browse for a file folder and store the folder path in an entry_box

    Parameters
    ----------
    entry_box : tkinter Entry widget
        Resulting folder path is stored here.

    Returns
    -------
        None    
    '''

    entry_box.delete(0,'end')
    src_folder = filedialog.askdirectory()
    entry_box.insert(0,src_folder)

def xfer_files(source, destination):
    '''Copy files younger than 1 day old from source to destination folder.

    Parameters
    ----------
    source : str
        Source folder from which to move files.
    destination : str
        Destination folder in which to move files to.

    Validation
    ----------
        Source and destination must be populated or an error message box is displayed.
        
    Returns
    -------
        None    
    '''
    
    print(source)
    print(destination)

    # if the source or destination is unpopulated, show a message box and return
    if(source=='' or destination ==''):
        messagebox.showerror(title='Error', message='Please select the Source and Destination paths.')
        return

    # if the source and destination are the same, show message box
    if(source == destination):
        messagebox.showerror(title='Error', message='Source and Destination paths must not be the same.')
        return

    # get list of files from source
    files = os.listdir(source)

    # in datetime format
    one_day_ago = (datetime.now()-timedelta(hours=24))#.timestamp() if I add this, it's in Epoch seconds
    print(one_day_ago)

    # Copy files to their destination if they are less than 24 hours old.
    for file_name in files:
        file_path = os.path.join(source, file_name)
        
        # Here are two ways to get a file's modification time
        # 1 Get all file stats, then pick out the mtime
        fileStatsObj = os.stat(file_path)  # gets all stats for the file.  All date/times in timestamp format
        print('file stats = {}'.format(fileStatsObj))
        file_stats_mod_date_in_sec = fileStatsObj.st_mtime
        mod_date_1 = datetime.fromtimestamp((file_stats_mod_date_in_sec)) # convert to datetime format
        print('mod_date_1 = {}'.format(mod_date_1))
        #print(type(fileStatsObj)) # <class 'os.stat_result'>
        # print(fileStatsObj.st_mtime) # mod time in seconds
        
        # Or 2 get just the modtime in timestamp format
        mod_date_in_sec = os.path.getmtime(file_path) # gets just modtime in timestamp format
        print(mod_date_in_sec)
        
        #mod_date = time.ctime(mod_date_in_sec) # string format returned by ctime can't be used to compare dates.
        mod_date = datetime.fromtimestamp((mod_date_in_sec)) # returns a datetime format from timestamp format
        
        print('File: {} \nMDate: {} \nMDate in Sec: {}\n'
              .format(file_path, mod_date, mod_date_in_sec))

        # if file mod date is less than one day ago, then move file to 2nd folder
        if(mod_date > one_day_ago):
            shutil.copy(file_path, destination) # Copy/overwrite file in destination
            print('Copied\n')
        else:
            print('Not Copied\n')

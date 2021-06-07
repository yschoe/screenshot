#!/usr/bin/python

"""
Save screenshot automatically to designated folder and prefix

  Enter [ESC] to exit.
  Enter [PrtScr] to capture and save to file
  - on some keyboards without [PrtScr], [Fn]-[Space] usually works.

Yoonsuck Choe
choe@tamu.edu

Fri, Feb 19, 2021  9:37:30 PM

"""

#----------------------------------------
# config : change this
#----------------------------------------
path   = 'C:/Users/loki/Pictures/'

#----------------------------------------
# import stuff
#----------------------------------------
from pynput.keyboard import Key, Controller, Listener
import pynput
import pyautogui, time
import sys
from datetime import datetime

#----------------------------------------
# main algorithm
#----------------------------------------

def on_press(key):

    if key == Key.print_screen:

        prefix = sys.argv[1]
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d--%H-%M-%S")
        fname = path+prefix+"-"+timestamp+".png"
        print("** Printscreen pressed!. Saving: "+fname)
        myScreenshot = pyautogui.screenshot(fname)

def on_release(key):

    if key == Key.esc:

        return False

with Listener(on_press=on_press,on_release=on_release) as listner:
  listner.join()


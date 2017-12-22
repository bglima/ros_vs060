# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 19:08:47 2017

@author: brunolima
"""

# mousepos.py (linux only)
"""module mousepos
"""
# uses the package python-xlib
# from http://snipplr.com/view/19188/mouseposition-on-linux-via-xlib/
from Xlib import display

display_dim = [2560.0, 1080.0] # Display dimensions X and Y
display_half = [ x * 0.5 for x in display_dim ] # Half of display dimensions
max_val = [15.0, 10.0] # Max value for linear and angular velocity 

def mousePos():
    """mousepos() --> (x, y) get the mouse coordinates on the screen (linux, Xlib)."""
    data = display.Display().screen().root.query_pointer()._data
    return data["root_x"], data["root_y"]
    
# Functions that transforms mouse coordinates from display to centered maxval space
def mouseFromCenter():
    pox_x, pos_y = mousePos()
    pos = [pos_x, pos_y]    
    tf = [ -max_val[i] * (pos[i] - display_half[i]) / display_half[i] for i in range(2) ]
    return tf[0], tf[1]
    
if __name__ == "__main__":
    print("The mouse position on the screen is {0}".format(mousePos()))
"""Raspberry Pi based Robot car control panel."""

"""
author : Ashraf Minhaj
mail   : ashraf_minhaj@yahoo.com
blog   : ashrafminhajfb.blogspot.com
"""

#import necessary libraries
#import necessary things from tkinter
#from tkinter import Tk, Button, Label
from tkinter import *         #import what necessary
from PIL import ImageTk       #for loading image


#load background and button images
backg_img = 'car.gif'
for_img = 'forward.gif'
left_img = 'left.gif'
right_img = 'right.gif'
back_img = 'back.gif'


def forward():
    """forward motion"""
    print("Going Forward Baby.")
    return

def backward():
    """backward motion"""
    print("Going back! Watch OUT!!")
    return

def left():
    """go left"""
    print("Going left Baby.")
    return

def right():
    """go right"""
    print("Going right man.")
    return


#initialize GUI
root = Tk()     #root is commonly used for instantiating tkinter

#set the window title
root.title("Robot Control Panel by Ashraf Minhaj")


#create a canvas with background image
canvas = Canvas(root, width=400, height=250)
canvas.pack()
img = ImageTk.PhotoImage(file=backg_img)
canvas.create_image(155,155 , image = img)

#read the image for tk
im_f = PhotoImage(file= for_img)
im_l = PhotoImage(file= left_img)
im_r = PhotoImage(file= right_img)
im_b = PhotoImage(file= back_img)

#buttons
for_but = Button(root,text="<< Left",repeatdelay=500,repeatinterval=100, command=forward)
for_but.config(image=im_f,borderwidth=0, bg='gray')
for_but_win = canvas.create_window(180, 10, anchor='nw', window=for_but)
#createwindow(row,column)

left_but = Button(root,text="<< Left",repeatdelay=500,repeatinterval=100, command=left)
left_but.config(image=im_l,borderwidth=1, bg='gray')
left_but_win = canvas.create_window(10, 115, anchor='nw', window=left_but)

right_but = Button(root,repeatdelay=500,repeatinterval=100, command=right)
right_but.config(image=im_r,borderwidth=0, bg='gray')
right_but_win = canvas.create_window(340, 115, anchor='nw', window=right_but)

back_but = Button(root, repeatdelay=500, repeatinterval=100, command=backward)
back_but.config(image=im_b,borderwidth=0, bg='gray')
back_but_win = canvas.create_window(180, 190, anchor='nw', window=back_but)

root.resizable(0,0)

root.mainloop()


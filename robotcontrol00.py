"""raspberry pi robot control panel with live video feed.
   Just like a video game control panel!
   *only this time the car/robot is real.

version: 4.f
1. seeing live feed, buttons overlayed
3. show notification on image
4. Control DC motors (making a full mobile robot)

author : Ashraf Minhaj
mail   : ashraf_minhaj@yahoo.com
"""

""" import necessary libraries """
import cv2                  
from tkinter import *  
from PIL import Image, ImageTk
import RPi.GPIO as pin    

""" variables """
# motor control pins
m11 = 8
m12 = 10
m21 = 12
m22 = 11

msg	  =''  # message variable
notif = ''

# load button icons
backg_img = 'res/car.gif'
for_img = 'res/f.gif'
left_img = 'res/l.gif'
right_img = 'res/r.gif'
back_img = 'res/b.gif'
quit_img = 'res/close.gif'

# cam feed variables
font = cv2.FONT_HERSHEY_SIMPLEX 
org = (30, 20) 
fontScale = 0.7
color = (255, 255, 255)
thickness = 2

""" setup things here """
pin.setwarnings(False)
pin.setmode(pin.BOARD)

# setup pins with initial state (LOW)
pin.setup(m11, pin.OUT, initial = pin.LOW)
pin.setup(m12, pin.OUT, initial = pin.LOW)
pin.setup(m21, pin.OUT, initial = pin.LOW)
pin.setup(m22, pin.OUT, initial = pin.LOW)

# read from camera 1
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 350)

""" initialize things """
root = Tk()
root.title("RPI Robot Control Panel by Ashraf Minhaj")

# main label for showing the feed (imagelabel)
imagel = Label(root)
imagel.pack()


def pin_state_low():
    """default state of certain pins, important for motors."""
    pin.output(m11, pin.LOW)
    pin.output(m12, pin.LOW)
    pin.output(m21, pin.LOW)
    pin.output(m22, pin.LOW)

def forward():
    """forward motion"""
    global msg
    msg = 'Going Forward'
    print(msg)
    
    pin.output(m11, pin.HIGH)
    pin.output(m21, pin.HIGH)
    return


def backward():
    """backward motion"""
    global msg
    msg = 'Going Backward'
    print(msg)
    
    pin.output(m12, pin.HIGH)
    pin.output(m22, pin.HIGH)
    return

def left():
    """go left"""
    global msg
    msg = 'Going Left'
    print(msg)
    
    pin.output(m12, pin.HIGH)
    pin.output(m21, pin.HIGH)
    return

def right():
    """go right"""
    global msg
    msg = 'Going Right'
    print(msg)

    pin.output(m11, pin.HIGH)
    pin.output(m22, pin.HIGH)
    return

def clear_msg():
    global msg
    msg = ''

def get_frame():
    """get a frame from the cam and return it."""
    # print("Getting image")
    ret, frame = cap.read()
    return frame

def update():
    """update frames"""
    global msg
    frame = get_frame()
    
    cv2.putText(frame, msg, org, font, fontScale, color, thickness, cv2.LINE_AA)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # manipulate image here 
    # to perfomr advanced CV operations

    # convert opencv image to tk image format
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)

    imagel.imgtk = imgtk
    imagel.configure(image=imgtk)

    # clear m
    clear_msg()
    
    # motor pins back to low state
    pin_state_low()
    
    # update frame after certain delay
    imagel.after(15, update)


# read the image for tk
im_f = PhotoImage(file= for_img)
im_l = PhotoImage(file= left_img)
im_r = PhotoImage(file= right_img)
im_b = PhotoImage(file= back_img)

im_quit = PhotoImage(file=quit_img)


# buttons
for_but = Button(root,text="<< Left",repeatdelay=15,repeatinterval=10, command=forward)
for_but.config(image=im_f, fg='gray', border=0, borderwidth=0, bg='black')
for_but.place(x=540, y=250)

left_but = Button(root,repeatdelay=15,repeatinterval=10, command=left)
left_but.config(image=im_l,border=0,borderwidth=0, bg='black' )
left_but.place(x=500, y=300)

right_but = Button(root,repeatdelay=15,repeatinterval=10, command=right)
right_but.config(image=im_r,border=0,borderwidth=0, bg='black')
right_but.place(x=580, y=300)

back_but = Button(root, repeatdelay=15, repeatinterval=10, command=backward)
back_but.config(image=im_b, border=0,borderwidth=0, bg='black')
back_but.place(x=540, y = 350)

quit_but = Button(root, text='Quit', command=root.destroy)
quit_but.config(image = im_quit, bg='red')
quit_but.place(x=0, y=0)

msg = ''
clear_msg()

update()

root.resizable(0, 0)

root.mainloop()
pin.cleanup()

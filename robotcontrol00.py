"""raspberry pi robot control panel with live video feed.
   Just like a video game control panel!
   *only this time the car/robot is real."""

"""
version: 4.f
1. seeing live feed, buttons over lapped
2. for controlling and interacting within the same window.
3. show notification on image
4. Control DC motors (making a full mobile robot)
"""


"""
author : Ashraf Minhaj
mail   : ashraf_minhaj@yahoo.com
blog   : ashrafminhajfb.blogspot.com
"""

import cv2   #open source computer vision library
from tkinter import *  #import only what necessary
from PIL import Image, ImageTk
import RPi.GPIO as pin    #import gpio control library

pin.setwarnings(False)
pin.setmode(pin.BOARD)

#motor control pins
m11 = 8
m12 = 10
m21 = 12
m22 = 11

#setup pins with initial state (LOW)
pin.setup(m11, pin.OUT, initial = pin.LOW)
pin.setup(m12, pin.OUT, initial = pin.LOW)
pin.setup(m21, pin.OUT, initial = pin.LOW)
pin.setup(m22, pin.OUT, initial = pin.LOW)

msg =''  #message variable

#width, height = 800, 500  #setting widht and height

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 350)

root = Tk()
root.title("RPI Robot Control Panel by Ashraf Minhaj")

#main label for showing the feed
imagel = Label(root)
imagel.pack()


# font 
font = cv2.FONT_HERSHEY_SIMPLEX 
# org 
org = (30, 20) 
# fontScale 
fontScale = 0.7
# Blue color in BGR 
color = (255, 255, 255)  
# Line thickness of 2 px 
thickness = 2


notif = ''

#load background and button images
backg_img = 'car.gif'
for_img = 'f.gif'
left_img = 'l.gif'
right_img = 'r.gif'
back_img = 'b.gif'
quit_img = 'close.gif'

msg = ''

def pins_default():
    """default state of certain pins, important for motors."""
    pin.output(m11, pin.LOW)
    pin.output(m12, pin.LOW)
    pin.output(m21, pin.LOW)
    pin.output(m22, pin.LOW)

def forward():
    """forward motion"""
    print("Going Forward Baby.")
    
    global msg
    msg = 'Going Forward'
    
    pin.output(m11, pin.HIGH)
    pin.output(m21, pin.HIGH)
    
    notlabel.config(text=" man keya liya hain")
    
    notif = 'shamne jai vai'
    
    return

def backward():
    """backward motion"""
    print("Going back! Watch OUT!!")
    
    global msg
    msg = 'Going BACKWARD'
    
    pin.output(m12, pin.HIGH)
    pin.output(m22, pin.HIGH)
    notlabel.config(text=" pichhe dekh madar toast")

    return

def left():
    """go left"""
    print("Going left Baby.")
    
    global msg
    msg = 'Going LEFT'
    
    pin.output(m12, pin.HIGH)
    pin.output(m21, pin.HIGH)
    notlabel.config(text=" dili to bam haat voira")
    notif = 'baaye jai vai'
    return

def right():
    """go right"""
    
    global msg
    msg = 'Going RIGHT'

    print("Going right man.")
    pin.output(m11, pin.HIGH)
    pin.output(m22, pin.HIGH)
    notlabel.config(text=" daye dekh")
    
    notif = 'dane jai vai'
    return

def msg_default():
    global msg
    msg = ''
    #return msg
  
def notification():
    global notif    #notification variable (global)
    

    return notif

def check_faces(f):  #check face upon given frame
    
    faces = face_cascade.detectMultiScale(f, scaleFactor = 1.5, minNeighbors = 5)
    #print(faces)
    for(x, y, w, h) in faces:

        print('Face found\n')
        #print(x, y, w, h)
        roi_f = f[y: y+h, x: x+w]  #region of interest is face
        
        #*** Drawing Rectangle ***
        color = (255, 0, 0)
        stroke = 2
        end_cord_x = x+w
        end_cord_y = y+h
        cv2.rectangle(f, (x,y), (end_cord_x, end_cord_y), color, stroke)
        
        return f
    

def get_frame():
    """get a frame from the cam and return it."""
    print("chhobi lagbo vai.")
    ret, frame = cap.read()
    
    return frame

def update():
    """update frames."""
    global msg
    print("dak porse vai")

    frame = get_frame()
    
    #if notification() != None:
    cv2.putText(frame, msg, org, font, fontScale, color, thickness, cv2.LINE_AA)
    
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #manipulate image here (if needed)
    #x = notification()
    #cv2.putText(frame, 'yahoo', org, font, fontScale, color, thickness, cv2.LINE_AA)
    
    

    try:
        cv2.image = check_faces(frame)
    except:
        pass


    img = Image.fromarray(cv2image)
    
    imgtk = ImageTk.PhotoImage(image=img)

    imagel.imgtk = imgtk
    imagel.configure(image=imgtk)
        
    msg_default()
    
    #motor pins back to default pos
    pins_default()
    
    imagel.after(15, update)


#read the image for tk
im_f = PhotoImage(file= for_img)
im_l = PhotoImage(file= left_img)
im_r = PhotoImage(file= right_img)
im_b = PhotoImage(file= back_img)

im_quit = PhotoImage(file=quit_img)


#buttons
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
msg_default()

update()

root.resizable(0, 0)

root.mainloop()
pin.cleanup()


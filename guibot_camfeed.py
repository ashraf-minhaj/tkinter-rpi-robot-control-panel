"""raspberry pi robot control panel with live video feed.
   Just like a video game control panel!
   *only this time the car/robot is real."""


#still on going **

"""
author : Ashraf Minhaj
mail   : ashraf_minhaj@yahoo.com
blog   : ashrafminhajfb.blogspot.com
"""

import cv2   #open source computer vision library
from tkinter import *  #import only what necessary
from PIL import Image, ImageTk

#width, height = 800, 500  #setting widht and height

cap = cv2.VideoCapture(0)   #get default camera feed

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)  
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 350)

#create the main window and set a title
root = Tk()
root.title("Robot Control Panel by Ashraf Minhaj")

#main label for showing the feed
imagel = Label(root)
imagel.pack()




#load background and button images
backg_img = 'car.gif'
for_img = 'f.gif'
left_img = 'l.gif'
right_img = 'r.gif'
back_img = 'b.gif'


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



def update():
    """update frames."""
    print("he called me broh!")

    ret, frame = cap.read()
    
    if ret:
        cv2iamge = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  #chaneg color of image from BGR to RGB
        img = Image.fromarray(cv2iamge)                    #convert array to image

        imgtk = ImageTk.PhotoImage(image=img)              #tkinter usable image

        imagel.imgtk = imgtk
        imagel.configure(image=imgtk)      #set the image on the label


    imagel.after(15, update)   #call after each 15 seconds


#read the image for tk
im_f = PhotoImage(file= for_img)
im_l = PhotoImage(file= left_img)
im_r = PhotoImage(file= right_img)
im_b = PhotoImage(file= back_img)



#buttons_____________________
"""create buttons and place them according to (row, column) value [pixel valueof your image size]"""
for_but = Button(root,text="<< Left",repeatdelay=500,repeatinterval=100, command=forward)
for_but.config(image=im_f, fg='gray', border=0,borderwidth=0, bg='black')
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
quit_but.config(width=2, height=1, fg='red',bg='black')
quit_but.place(x=0, y=0)

update()     #look for new image frame

root.resizable(0, 0)   #resrict window from resizing
root.mainloop()
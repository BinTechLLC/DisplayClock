#!/usr/bin/env python3.7
from tkinter import *
import time
from time import gmtime, strftime
import os
fullScreenMode=False
utcTime=''
localTime=''
def showUTCTime():
    global utcTime
    utcTime=time.strftime('%H:%M:%S', gmtime()) # Change the %H to %l for 12 hour format.
    utcClock.configure(text=utcTime)
    utcClock.after(100, showUTCTime)
    return
def showLocalTime():
    global localTime
    localTime=time.strftime('%l:%M:%S') # Change the %H to %l for 12 hour format.
    localClock.configure(text=localTime)
    localClock.after(100, showLocalTime)
    return
def programExit():
    root.destroy()
    exit()
    return
root=Tk()
root.title("Time Display")
root.geometry("800x480+0+0")    # Resolution, Start X Position, Start Y Position.
root.attributes('-fullscreen', fullScreenMode)
root.configure(background="gray1")

utcClock=Label(root,font=("Helvetica","26"),width=20,height=2,bd=1,bg="orange2",fg="gray99")
utcClock.place(x=5,y=5)

localClock=Label(root,font=("Helvetica","26"),width=20,height=2,bd=1,bg="green2",fg="gray99")
localClock.place(x=5,y=100)

exitButton=Button(root,text="EXIT",font=("Helvetica","14"),width=6,height=2,bd=1,bg="gray1",fg="gray99",activebackground="gray30",activeforeground="red",command=programExit)
exitButton.place(x=705,y=400)

showUTCTime()
showLocalTime()
root.mainloop()

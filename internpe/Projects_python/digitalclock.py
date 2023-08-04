from tkinter import Tk ## tk is used to make window on which our clock will display
from tkinter import Label ##label is used whwnever we have to write something on that window
import time


root = Tk()
root.title("Clock")#title of the window that will display

def present_time():
    display_time = time.strftime("%H:%M :%S %p") ##strftime is used to give current time,%I is used to whwn we want to display our time from 1 to 9 And %H for 1 to 24
    digi_clock.config(text=display_time)
    digi_clock.after(200 ,present_time) ## 200 millisecond after every 200 ms my time will run

digi_clock = Label(root, font=("arial, 50"), bg="green" ,fg="black")
digi_clock.pack()

present_time()


root.mainloop()
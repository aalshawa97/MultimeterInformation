import time
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Welcome!")

def showImage():
    img = PhotoImage(file=r"MULTIMETER IMAGE FILE PATH HERE")
    button = Button(root, image=img)
    button.img = img  # Keep a reference!
    button.grid()

def switch(menu):
    if menu == "1":
        label = Label(root, text="Multimeters measure electrical properties such as voltage, current, and resistance.\n"
                                 "Current is a measure of the rate at which electric charge flows past a specific point in a circuit.\n"
                                 "Resistance is a measure of how much the flow of electrons is slowed down, measured in ohms.\n"
                                 "Voltage is the measure of electrical potential difference that pushes electrons through a circuit.\n"
                                 "V = I(current) * R(resistance)")
        label.grid()
    else:
        showImage()

# GUI-based input instead of console
label = Label(root, text="Press 1 if you would like to learn about multimeters. Press 2 if you would like see an image of a multimeter. Press the X in the top right corner to exit.",)
label.grid()

entry = Entry(root)
entry.grid()

def on_submit():
    user_input = entry.get()
    switch(user_input)

submit_button = Button(root, text="Submit", command=on_submit)
submit_button.grid()

root.mainloop()

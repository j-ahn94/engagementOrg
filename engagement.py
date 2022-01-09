""" engagement.py is a program dedicated to PwC for measuring the amount of time spent
    for each engagement.
"""

import tkinter as tk
from tkinter import filedialog, Text
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime

import os

# create GUI window
root = tk.Tk()
root.title('PwC - Stopwatch')
root.resizable(0, 0)

canvas = tk.Canvas(root, height = 500, width = 800, bg = "white")

canvas.pack()
#canvas.title("PwC Engagement")


#path = "pwc_logo.png"
#img = ImageTk.PhotoImage(Image.open(path))

img = (Image.open("pwc_logo2.png"))
#img = ImageTk.PhotoImage(Image.open("pwc_logo.png"))

#canvas.create_image(0.1, 0.1, anchor= tk.W, image = img)


frame1 = tk.Frame(root, bg = "yellow")
frame1.place(relwidth = 0.45, relheight = 0.9, rely = 0.10, relx = 0.05)

frame2 = tk.Frame(root, bg = "green")
frame2.place(relwidth = 0.4, relheight = 0.9, rely = 0.10, relx = 0.53)

resized_pwc_image = img.resize((75, 45), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_pwc_image)

#frame.create_image(10, 10, anchor=tk.NW, image=new_image)

#Display PwC logo image
label = tk.Label(canvas, image = new_image)
label.image = new_image
label.place(x = 1, y = 1)


def tick():
    now = datetime.now().strftime('%B %d \n %A')
    clock.config(text=now)
    clock.after(200, tick)
    

clock = tk.Label(frame1, font=("none", 20, "bold"), bg = "white", fg = "black", anchor = CENTER)
clock.grid(row = 0, column = 0)


tick()




#WORK ON THIS SUNDAY

""" img2 = PhotoImage(file = "stopwatch_circle.png")
frame1.place.create_image(20, 20, anchor=NW, image =img2) """

img2 = Image.open("stopwatch_circle.png")

resized_circle_image = img2.resize((325, 350), Image.ANTIALIAS)

render = ImageTk.PhotoImage(resized_circle_image)
stopwatch = Label(frame1, image=render)
stopwatch.place(x= 30, y = 70)




addButton = tk.Button(frame1, text = "CREATE", fg = "red", height = 1, width = 15)
addButton.place(x = 140, y= 400)


#frame.create_image(10, 10, anchor=tk.NW, image=new_image)

#Display PwC logo image
""" label = tk.Label(canvas, image = new_image)
label.image = new_image
label.place(x = 1, y = 1) """



""" # create text field when clicking a 'Add' button
entry1 = tk.Entry(root)

def textBoxCreate():
    canvas.create_window(200, 140, window = entry1) """

# button to quit the program
""" quitButton = tk.Button(frame, text = "QUIT", fg = "red", command = quit)
quitButton.pack(side = tk.BOTTOM, padx = 10, pady = 10)

# button to add engagement
addButton = tk.Button(frame, text = "CREATE", fg = "red", command = textBoxCreate)
addButton.pack(side = tk.BOTTOM) """


def write_slogan():
    print("Tkinter is easy to use!")

slogan = tk.Button(frame1,
                text = "Hello",
                command=write_slogan)


root.mainloop()
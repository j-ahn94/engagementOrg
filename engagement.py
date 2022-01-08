import tkinter as tk
from tkinter import filedialog, Text
from pil import ImageTk, Image

import os

# create GUI window
root = tk.Tk()

canvas = tk.Canvas(root, height = 500, width = 400, bg = "grey")
canvas.pack()
#canvas.title("PwC Engagement")

path = "pwc_logo.png"
img = ImageTk.PhotoImage(Image.open(path))

frame = tk.Frame(root, bg = "lightgrey")
frame.place(relwidth = 0.8, relheight = 0.8, rely = 0.1, relx = 0.1)

# create text field when clicking a 'Add' button
entry1 = tk.Entry(root)

def textBoxCreate():
    canvas.create_window(200, 140, window = entry1)

# button to quit the program
quitButton = tk.Button(frame, text = "QUIT", fg = "red", command = quit)
quitButton.pack(side = tk.BOTTOM, padx = 10, pady = 10)

# button to add engagement
addButton = tk.Button(frame, text = "CREATE", fg = "red", command = textBoxCreate)
addButton.pack(side = tk.BOTTOM)



def write_slogan():
    print("Tkinter is easy to use!")

slogan = tk.Button(frame,
                text = "Hello",
                command=write_slogan)

root.mainloop()



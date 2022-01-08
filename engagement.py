import tkinter as tk
from tkinter import filedialog, Text
from PIL import ImageTk, Image

import os

# create GUI window
root = tk.Tk()

canvas = tk.Canvas(root, height = 500, width = 400, bg = "grey")
canvas.pack()
#canvas.title("PwC Engagement")


#path = "pwc_logo.png"
#img = ImageTk.PhotoImage(Image.open(path))

img = (Image.open("pwc_logo.png"))
#img = ImageTk.PhotoImage(Image.open("pwc_logo.png"))

#canvas.create_image(0.1, 0.1, anchor= tk.W, image = img)


frame = tk.Frame(root, bg = "lightgrey")
frame.place(relwidth = 0.8, relheight = 0.8, rely = 0.1, relx = 0.1)

resized_image = img.resize((80, 50), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)

#frame.create_image(10, 10, anchor=tk.NW, image=new_image)

#Display PwC logo image
label = tk.Label(frame, image = new_image)
label.image = new_image
label.place(x = 1, y = 1)


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



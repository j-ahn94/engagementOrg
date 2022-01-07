import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

canvas = tk.Canvas(root, height = 500, width = 400, bg = "grey")
canvas.pack()

frame = tk.Frame(root, bg = "lightgrey")
frame.place(relwidth = 0.8, relheight = 0.8, rely = 0.1, relx = 0.1)

root.mainloop()


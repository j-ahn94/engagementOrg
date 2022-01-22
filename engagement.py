""" engagement.py is a program dedicated to PwC for measuring the amount of time spent
    for each engagement.
"""

import tkinter as tk

from tkinter import filedialog, Text, ttk
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime

import os

# create GUI window
root = tk.Tk()
root.title('PwC - Stopwatch')
root.resizable(0, 0)

canvas = tk.Canvas(root, height = 500, width = 800)

canvas.pack()

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
clock.place(x = 110, y = 2)

tick()

# label to display time
""" stopwatch_label = tk.Label(frame1, text = '00:00:00', font = ('Arial', 30), bg = "green")
stopwatch_label.place(x=50,y=40) """


#WORK ON THIS SUNDAY


img2 = Image.open("circle.png")

resized_circle_image = img2.resize((325, 350), Image.ANTIALIAS)

render = ImageTk.PhotoImage(resized_circle_image)
stopwatch = tk.Label(frame1, image=render)
stopwatch.place(x= 30, y = 70)

""" lbl = Label(
    root,
    text="00",
    fg="black",
    bg="#299617",
    font="Verdana 100 bold"
    )

lbl.place(x=160, y=170)
 """

counter = -1

hours, minutes, seconds = 0, 0, 0

running = False

#NEW

def pause():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False

   
def start():
    global running
    if not running:
        counter_label()
        running = True
    start_button.pack_forget()

    pause_button = tk.Button(frame1, text = "pause", height = 2, width = 10, font = ('Arial', 10), command = pause)

    pause_button.pack(side = BOTTOM)

    """ start_button.place(x = 100, y = 300) """


#NEW
def counter_label():
    global hours, minutes, seconds
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'

    stopwatch_label.config(text=hours_string + ":" + minutes_string + ":" + seconds_string)

    global update_time
    update_time = stopwatch_label.after(1000, counter_label)

information = tk.Label(text = 'PLEASE SELECT A TASK', font=('Arial', 9))
information.place(x = 160, y = 250)

t2 = tk.Text()
t2.place(x = 160, y = 250)
t2.place_forget()

stopwatch_label = tk.Label(text='00:00:00', font=('Arial', 20))
stopwatch_label.place(x = 190, y = 280)

start_button = tk.Button(frame1, text = "start", height = 2, width = 10, font = ('Arial', 10), command = start)

""" start_button.place(x = 100, y = 300) """

start_button.pack(side = BOTTOM)


tabControl = ttk.Notebook(frame2)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text = 'TASKS')
tabControl.add(tab2, text = 'STATISTICS')

tabControl.pack(expand = 1, fill = 'both', ipadx = 50)

ttk.Label(tab1,
        text = "TASKS", font = '50').grid(column = 0,
                            row = 0,
                            padx = 20,
                            pady = 10)

my_entries = []
count = 0

""" def delete():
    my_entries.delete(0, tk.END) """

""" def select(select_button):
    select_button.place_forget()
    information.destroy()

    for x in range(len(my_entries)):
        t2.insert(1.0, my_entries[x]) """

""" def my_upd():
    global count
    

    MAXIMUM = 360
    if count <= MAXIMUM:
        my_entries.append(Text(frame2, width = 23, height = 1, padx = 10, pady = 5).place(x = 30, y = 75 + count))
        
        select_button = Button(frame2, text = "SELECT", command = lambda:select(select_button), width = 5, height = 1, bg = 'white')
        
        
        select_button.place(x = 250, y = 75 + count)
        
        count += 40 """

    #Text(frame2, width = 30, height = 1).place(x = 30, y = 75)

""" Button(tab1, text='-', bg = 'yellow', command = lambda:delete()).place(x = 270, y = 10) """

my_entries.append(Text(frame2, width = 23, height = 1, padx = 10 , pady = 5).place(x = 30, y = 75))

Button(tab1, text='SELECT', bg = 'yellow', command = lambda: insertItem).place(x = 250, y = 50)

ttk.Label(tab2,
        text = "Welcome to GeeksBruh").grid(column = 0,
                            row = 0,
                            padx = 30,
                            pady = 30)

""" def counter_label(lbl):
    def count():
        if running:
            global counter
            if counter == -1:
                display = "00:"
            else:
                display = str(counter)
            lbl['text'] = display

            lbl.after(1000, count)
            counter += 1
    count() """

""" def StartTimer(lbl):
    global running
    running = True
    counter_label(lbl)
    addButton['state'] = 'disabled' """

""" addButton = Button(
    root,
    text="START",
    width= 15,
    height = 1,
    command=lambda:StartTimer(lbl) 
)

addButton.place(x = 140, y = 400)

addButton = tk.Button(frame1, text = "START", fg = "red", height = 1, width = 15) """


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


""" def write_slogan():
    print("Tkinter is easy to use!")

slogan = tk.Button(frame1,
                text = "Hello",
                command=write_slogan) """


root.mainloop()
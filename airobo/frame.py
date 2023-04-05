#!/usr/bin/env python3

import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

window = tk.Tk()

window.title("Future City")
window.geometry("800x900+100+100")
window.configure(bg="black")

# img = ImageTk.PhotoImage(Image.open("kobe_bryant.jpg"))
img = ImageTk.PhotoImage(Image.open("kobe_24.gif"))

label = Label(window, image = img)
label.pack()

window.mainloop()
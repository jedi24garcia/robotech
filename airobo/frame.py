#!/usr/bin/env python3

import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

window = tk.Tk()

window.title("Black Mamba")
window.geometry("800x900+100+100")
window.configure(bg="black")

# img = ImageTk.PhotoImage(Image.open("kobe_bryant.jpg"))
img = ImageTk.PhotoImage(Image.open("kobe_bryant.jpg"))

label = Label(window, image = img)
label.pack()

window.mainloop()
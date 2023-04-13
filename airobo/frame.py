#!/usr/bin/env python3

import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
# from self import speak

window = tk.Tk()
frm = ttk.Frame(window, padding=0)

window.title("Black Mamba")
window.geometry("800x500+50+50")
window.configure(bg="black")

ttk.Label(frm, text="Hello, user").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=window.destroy).grid(column=1, row=0)

# img = ImageTk.PhotoImage(Image.open("kobe_bryant.jpg"))
# img = ImageTk.PhotoImage(Image.open("kobe_bryant.jpg"))

# label = Label(window, image = img)
# label.pack()
frm.grid()
window.mainloop()
#!/usr/bin/env python3

import tkinter as tk
from tkinter import *
# from PIL import ImageTK, Image
from PIL import Image, ImageTk

window = tk.Tk()

window.title("Kobe")
window.geometry("500x400")
window.configure(bg="black")

img = ImageTk.PhotoImage(Image.open("cool_city.jpg"))

window.mainloop()
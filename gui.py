from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window["background"] = "#35654d"

image2C = Image.open("images/2C.png")
image2D = Image.open("images/2D.png")
test2 = ImageTk.PhotoImage(image2D)
test = ImageTk.PhotoImage(image2C)

label1 = tk.Label(image=test)
label1.image = test


label1.pack()

window.mainloop()

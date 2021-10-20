from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window["background"] = "#35654d"


class ImageClass:
    def process_images(self, num_images):
        self.images = []
        for i in range(num_images):
            image_filename = "images/image%s.png" % i
            number_img = Image.open(image_filename)
            number_img = ImageTk.PhotoImage(number_img)
            self.images.append(number_img)


c = ImageClass()
c.process_images(2)

#image2C = Image.open("images/image0.png")
#image2D = Image.open("images/image1.png")
#test2 = ImageTk.PhotoImage(image2D)
#test = ImageTk.PhotoImage(image2C)

#label1 = tk.Label(image=test)

label1 = tk.Label(image=c.images[0])


def onclick():
    label1.config(image=c.images[1])


btn = Button(window, text="Change Card", command=onclick)

label1.pack()
btn.pack()
window.mainloop()

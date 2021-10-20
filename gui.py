from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import main

# Creating the tkinter window and setting background color to standard blackjack table
window = tk.Tk()
window["background"] = "#35654d"


# Indexing the value of the cards to the images
Card_img_index = {
            'Clubs of Two': 1,
            'Clubs of Three': 2,
            'Clubs of Four': 3,
            'Clubs of Five': 4,
            'Clubs of Six': 5,
            'Clubs of Seven': 6,
            'Clubs of Eight': 7,
            'Clubs of Nine': 8,
            'Clubs of Ten': 9,
            'Clubs of Jack': 10,
            'Clubs of Queen': 11,
            'Clubs of King': 12,
            'Clubs of Ace': 13,
            'Diamonds of Two': 14,
            'Diamonds of Three': 15,
            'Diamonds of Four': 16,
            'Diamonds of Five': 17,
            'Diamonds of Six': 18,
            'Diamonds of Seven': 19,
            'Diamonds of Eight': 20,
            'Diamonds of Nine': 21,
            'Diamonds of Ten': 22,
            'Diamonds of Jack': 23,
            'Diamonds of Queen': 24,
            'Diamonds of King': 25,
            'Diamonds of Ace': 26,
            'Hearts of Two': 27,
            'Hearts of Three': 28,
            'Hearts of Four': 29,
            'Hearts of Five': 30,
            'Hearts of Six': 31,
            'Hearts of Seven': 32,
            'Hearts of Eight': 33,
            'Hearts of Nine': 34,
            'Hearts of Ten': 35,
            'Hearts of Jack': 36,
            'Hearts of Queen': 37,
            'Hearts of King': 38,
            'Hearts of Ace': 39,
            'Spades of Two': 40,
            'Spades of Three': 41,
            'Spades of Four': 42,
            'Spades of Five': 43,
            'Spades of Six': 44,
            'Spades of Seven': 45,
            'Spades of Eight': 46,
            'Spades of Nine': 47,
            'Spades of Ten': 48,
            'Spades of Jack': 49,
            'Spades of Queen': 50,
            'Spades of King': 51,
            'Spades of Ace': 52
}


# Open and process the images
class ImageClass:
    def process_images(self, num_images):
        self.images = []
        for i in range(num_images):
            image_filename = "images/image%s.png" % i
            number_img = Image.open(image_filename)
            number_img = ImageTk.PhotoImage(number_img)
            self.images.append(number_img)


c = ImageClass()
c.process_images(53)


# Testing
deck_one = main.Deck()
deck_one.shuffle()
print(deck_one.deck.keys())
print(Card_img_index.values())

card = main.Card(deck_one.deal())
print(card.name)

label1 = tk.Label(image=c.images[0])

if card.name in Card_img_index:
    print("It worked")
    label1.config(image=c.images[Card_img_index.get(card.name)])
else:
    print("It failed")




def onclick():
    label1.config(image=c.images[5])


btn = Button(window, text="Change Card", command=onclick)


label1.pack()
btn.pack()
window.mainloop()

# File-name: Book_class.py
# Author: Nea Träskman and Melina Kamunen
# Description:
import os
import tkinter as tk
from tkinter import *
import Gui_class
import Loan_class

class Book_page():
    def __init__(self):
        tk.Frame.__init__(self)

        # image label
        #bg_label = tk.Label(self, image = Gui_class.img)
        #bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        text3_label = tk.Label(self, text="Do you wan't to loan books movies or magazines?", bg="white", fg="black", font=('Helvetica', '15', 'bold'))
        text3_label.pack(pady=10,padx=10)

        base_folder = os.path.dirname(__file__)
        
        # Importing images to be used as a buttons
        book_image_path = os.path.join(base_folder, 'book_icon.png')
        self.Book_Image = tk.PhotoImage(file = book_image_path)
        self.Book_Icon = self.Book_Image.subsample(7, 5) # Resizing the image to fit on the button

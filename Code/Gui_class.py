from tkinter import *

class App(Tk):

    def __init__(self):
        super().__init__()

        self.geometry("300x250") # setting the size of the GUI window
        self.title("Library - Login") # title of the GUI window

        #creating the form label
        self.label = Label(text="Login or Register", bg="gray", width="300", height="2", font=("Calibri", 12))
        self.label.pack()

        # creating the login button
        self.button = Button(text="Login", height="2", width="30")
        self.button.pack()

        # creating the register button
        Button(text="Register", height="2", width="30").pack()


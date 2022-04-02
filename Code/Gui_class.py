from tkinter import *

class App(Tk):

    def __init__(self):
        super().__init__()

        self.geometry("800x500") # setting the size of the GUI window
        self.title("Library - Login") # title of the GUI window

        global bg
        bg = PhotoImage(file = "Code/library_pic.png")

        self.label = Label(self, image= bg)
        self.label.place(x=0, y=0, relwidth=1, relheight=1)

        # creating the login button
        #self.button = Button(text="Login", height="2", width="30")
        #self.button.place(pady=20)

        # creating the register button
        #self.button = Button(text="Register", height="2", width="30")
        #self.button.place(pady=20)


from tkinter import *

class App(Tk):

    def __init__(self):
        super().__init__()

        self.geometry("612x459") # setting the size of the GUI window
        self.title("E-Library - Login") # title of the GUI window
        self.resizable(False, False)

        global bg
        bg = PhotoImage(file = "Code/library_photo.png")

        self.label = Label(self, image= bg)
        self.label.place(x=0, y=0, relwidth=1, relheight=1)

        # Adding a text box on top of our image
        self.text_box = Label(self, text="E-Library", font="helvetica 32 bold", fg="black", bg = "white")
        self.text_box.pack(pady=30)

        # creating the login button
        self.button_login = Button(text="Login", height="2", width="20")
        self.button_login.pack(pady=20)

        # creating the register button
        self.button_register = Button(text="Register", height="2", width="20")
        self.button_register.pack(pady=20)


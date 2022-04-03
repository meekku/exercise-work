import tkinter as tk
from tkinter import *

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.geometry("600x400") # setting the size of the GUI window
        self.title("E-Library") # title of the GUI window
        self.resizable(False, False)

        #importing image
        #global image
        #image = PhotoImage(file = "Code/library_photo.png")

        #creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #Initialize frames
        self.frames = {}

        #Defining frames and packing it
        for F in (HomePage, Page_Login):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(HomePage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="E-Library", font=('Helvetica', '32', 'bold'))
        label.pack(pady=10,padx=10)

        # creating the login button
        Button_Login = tk.Button(text="Login", height="2", width="20",
        command=lambda: controller.show_frame(Page_Login))
        Button_Login.pack(pady=10)

        # creating the register button
        Button_Register = tk.Button(text="Register", height="2", width="20")
        Button_Register.pack(pady=10)


class Page_Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="E-Library Login", font=('Helvetica', '32', 'bold'))
        label.pack(pady=10,padx=10)

        back_button = tk.Button(self, text='Go back', 
        command=lambda: controller.show_frame(HomePage))
        back_button.pack(pady=10)



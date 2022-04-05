import tkinter as tk
from tkinter import *
import os

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.geometry("600x400") # setting the size of the GUI window
        self.title("E-Library") # title of the GUI window
        self.resizable(False, False)

        #creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #Initialize frames
        self.frames = {}

        #Defining frames and packing it
        for F in (HomePage, Page_Login, Page_Register):
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

        # these lines help to find image
        global img
        base_folder = os.path.dirname(__file__)
        image_path = os.path.join(base_folder, 'library_photo.png')
        img = PhotoImage(file=image_path)

        # image label
        bg_label = tk.Label(self, image = img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # text label
        text_label = tk.Label(self, text="E-Library", bg="white", fg="black", font=('Helvetica', '32', 'bold'))
        text_label.pack(pady=10,padx=10)

        # creating the login button
        Button_Login = tk.Button(self, text="Login", height="2", width="20",
        command=lambda: controller.show_frame(Page_Login))
        Button_Login.pack(pady=10)

        # creating the register button
        Button_Register = tk.Button(self, text="Register", height="2", width="20",
        command=lambda: controller.show_frame(Page_Register))
        Button_Register.pack(pady=10)

class Page_Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # image label
        bg_label = tk.Label(self, image = img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        text2_label = tk.Label(self, text="E-Library Login", bg="white", fg="black", font=('Helvetica', '32', 'bold'))
        text2_label.pack(pady=10,padx=10)

        username_login = StringVar()
        password_login = StringVar()

        login_label = tk.Label(self, text="Please enter details below to login", bg="white", fg="black", 
        font=('Helvetica', '16'))
        login_label.pack(pady=10)

        Label(self, text="Username * ", bg="white", fg="black").pack()
        username_login_entry = tk.Entry(self, textvariable=username_login, bg="white", fg="black")
        username_login_entry.pack()
        Label(self, text="", bg="white", fg="black").pack()
        Label(self, text="Password * ", bg="white", fg="black").pack()
        password__login_entry = tk.Entry(self, textvariable=password_login, show= '*', bg="white", fg="black")
        password__login_entry.pack()
        Label(self, text="", bg="white", fg="black").pack()

        # Set login button
        login_button = tk.Button(self, text='Login', height="2", width="20",
        command=lambda: controller.show_frame(HomePage))
        login_button.pack(pady=10)

        back_button = tk.Button(self, text='Go back', height="2", width="20", 
        command=lambda: controller.show_frame(HomePage))
        back_button.pack(pady=10)

class Page_Register(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # image label
        bg_label = tk.Label(self, image = img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        text3_label = tk.Label(self, text="E-Library Register", bg="white", fg="black", font=('Helvetica', '32', 'bold'))
        text3_label.pack(pady=10,padx=10)

        username = StringVar()
        password = StringVar()

        # Set label for user's instruction
        register_label = tk.Label(self, text="Please enter details below", bg="white", fg="black", 
        font=('Helvetica', '16'))
        register_label.pack(pady=10)
        # Set username label
        username_lable = tk.Label(self, text="Username * ", bg="white", fg="black")
        username_lable.pack()
        # Set username entry
        username_entry = tk.Entry(self, textvariable=username, bg="white", fg="black")
        username_entry.pack()
        # Set password label
        password_lable = tk.Label(self, text="Password * ", bg="white", fg="black")
        password_lable.pack()
        # Set password entry
        password_entry = tk.Entry(self, textvariable=password, show='*', bg="white", fg="black")
        password_entry.pack()
        
        Label(self, text="", bg="white").pack()
        
        # Set register button
        register_button = tk.Button(self, text='Register', height="2", width="20",
        command=lambda: controller.show_frame(HomePage))
        register_button.pack(pady=10)

        back_button = tk.Button(self, text='Go back', height="2", width="20",
        command=lambda: controller.show_frame(HomePage))
        back_button.pack(pady=10)

class User_Validation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


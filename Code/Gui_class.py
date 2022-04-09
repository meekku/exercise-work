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
        container.configure(bg="white")

        #Initialize frames
        self.frames = {}

        #Defining frames and packing it
        for F in (HomePage, Page_Login, Page_Register, Library_Page):
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

        # these lines help to find the image within the files
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

        # creating the exit button
        Close_App = tk.Button(self, text= "Exit", height="2", width="20", 
        command=self.quit)
        Close_App.pack(pady=20)

class Page_Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # image label
        bg_label = tk.Label(self, image = img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        text2_label = tk.Label(self, text="E-Library Login", bg="white", fg="black", font=('Helvetica', '32', 'bold'))
        text2_label.pack(pady=10,padx=10)

        self.username_login = StringVar()
        self.password_login = StringVar()

        login_label = tk.Label(self, text="Please enter details below to login", bg="white", fg="black", 
        font=('Helvetica', '16'))
        login_label.pack(pady=10)

        Label(self, text="Username * ", bg="white", fg="black").pack()
        self.username_login_entry = tk.Entry(self, textvariable=self.username_login, bg="white", fg="black")
        self.username_login_entry.pack()
        Label(self, text="", bg="white", fg="black").pack()
        Label(self, text="Password * ", bg="white", fg="black").pack()
        self.password_login_entry = tk.Entry(self, textvariable=self.password_login, show= '*', bg="white", fg="black")
        self.password_login_entry.pack()
        Label(self, text="", bg="white", fg="black").pack()

        # Set login button
        login_button = tk.Button(self, text='Login', height="2", width="20",
        command=self.login_verify)
        login_button.pack(pady=10)

        back_button = tk.Button(self, text='Go back', height="2", width="20", 
        command=lambda: controller.show_frame(HomePage))
        back_button.pack(pady=10)
    
    def login_verify(self):

        # get the username and the password
        verify_username = self.username_login.get()
        verify_password = self.password_login.get()

        # deletes the entries after login button is pressed
        self.username_login_entry.delete(0, END)
        self.password_login_entry.delete(0, END)

        list_of_files = os.listdir()

        if verify_username in list_of_files:
            file1 = open("user_information.txt", "r")   # open the file in read mode
            verify = file1.read().splitlines()

            if verify_password in verify:
                self.login_success()
            else:
                self.password_not_correct()
        else:
            self.user_not_found()
    

    def login_success(self):
        # user succesfully logins to the e-library and is moved to library page
        pass
    def password_not_correct(self):
        # tells user the password was incorrect
        # returns to login page
        pass
    def user_not_found(self):
        #code if the user wasnt found in the file
        #gets a pop up telling not found and returns back to login page
        pass

class Page_Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # image label
        bg_label = tk.Label(self, image = img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.text3_label = tk.Label(self, text="E-Library Register", bg="white", fg="black", font=('Helvetica', '32', 'bold'))
        self.text3_label.pack(pady=10,padx=10)

        self.username = StringVar()
        self.password = StringVar()

        # Set label for user's instruction
        register_label = tk.Label(self, text="Please enter details below", bg="white", fg="black", 
        font=('Helvetica', '16'))
        register_label.pack(pady=10)
        # Set username label
        username_lable = tk.Label(self, text="Username * ", bg="white", fg="black")
        username_lable.pack()
        # Set username entry
        self.username_entry = tk.Entry(self, textvariable=self.username, bg="white", fg="black")
        self.username_entry.pack()
        # Set password label
        password_lable = tk.Label(self, text="Password * ", bg="white", fg="black")
        password_lable.pack()
        # Set password entry
        self.password_entry = tk.Entry(self, textvariable=self.password, show='*', bg="white", fg="black")
        self.password_entry.pack()
        
        Label(self, text="", bg="white").pack()
        
        # Set register button
        register_button = tk.Button(self, text='Register', height="2", width="20",
        command= self.User_Registration)
        register_button.pack(pady=10)

        back_button = tk.Button(self, text='Go back', height="2", width="20",
        command=lambda: controller.show_frame(HomePage))
        back_button.pack(pady=10)
    
    def User_Registration(self):

        # get the username and password
        get_username = self.username.get()
        get_password = self.password.get()

        # open file where the data goes
        user_file = open("Code/user_information.txt", "a+")
        print("File opened.")
        user_file.write(get_username + "\n")
        user_file.write(get_password)
        print("Closing file.")
        user_file.close()

        # makes the entries empty
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
    
    def Reg_Confirmation(self): # Registration confirmation for the user

        # Here some code that will tell the user the registration has completed
        # and it returns them to the main page
        pass

class Library_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # image label
        bg_label = tk.Label(self, image = img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        text3_label = tk.Label(self, text="Choose what you want to loan", bg="white", fg="black", font=('Helvetica', '32', 'bold'))
        text3_label.pack(pady=10,padx=10)

        # Importing images to be used as a buttons
        self.Book_Image = tk.PhotoImage(file = r"Code/book_icon.png")
        self.Book_Icon = self.Book_Image.subsample(6, 6) # Resizing the image to fit on the button
        self.Movie_Image = tk.PhotoImage(file = r"Code/movie_icon.png")
        self.Movie_Icon = self.Movie_Image.subsample(6, 6)
        self.Magazine_Image = tk.PhotoImage(file = r"Code/magazine_icon.png")
        self.Magazine_Icon = self.Magazine_Image.subsample(15, 15)

        Book_Button = tk.Button(self, text = "Books", image = self.Book_Icon)
        Book_Button.place(x=60, y=80)

        Movie_Button = tk.Button(self, text = "Movies", image = self.Movie_Icon)
        Movie_Button.place(x=235, y=80)

        Magazine_Button = tk.Button(self, text = "Magazines", image = self.Magazine_Icon)
        Magazine_Button.place(x=395, y=80)

        log_out_button = tk.Button(self, text='Log out', height="2", width="20",
        command=lambda: controller.show_frame(HomePage))
        log_out_button.place(x=200, y=330)



        

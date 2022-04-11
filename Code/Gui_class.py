import tkinter as tk
from tkinter import *
import os
import Book_class
import ast

from setuptools import Command

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
        for F in (HomePage, Page_Login, Page_Register, Library_Page, BookPage):
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

        # Set username label
        username_lable = tk.Label(self, text="Username * ", bg="white", fg="black")
        username_lable.pack()
        # Set username_login entry
        self.username_login_entry = tk.Entry(self, textvariable=self.username_login, bg="white", fg="black")
        self.username_login_entry.pack()

        # Set password label
        password_lable = tk.Label(self, text="Password * ", bg="white", fg="black")
        password_lable.pack()
        # Set password_login entry
        self.password_login_entry = tk.Entry(self, textvariable=self.password_login, show='*', bg="white", fg="black")
        self.password_login_entry.pack()

        # Set login button
        login_button = tk.Button(self, text='Login', height="2", width="20",
        command=lambda: self.login_verify(controller))
        login_button.pack(pady=10)

        # Set return button
        back_button = tk.Button(self, text='Go back', height="2", width="20", 
        command=lambda: controller.show_frame(HomePage))
        back_button.pack(pady=10)
    
    def login_verify(self,controller): 
        
        # get the username and the password
        verify_username = self.username_login.get()
        verify_password = self.password_login.get()
        combination = verify_username + ":" + verify_password
        found = False

        # finding the file where user information is
        base_folder = os.path.dirname(__file__)
        list_of_files = os.path.join(base_folder, 'user_information.txt')
        opened_file = open(list_of_files, "r")   # open the file in read mode

        # reading lines from file and finding match for combination
        for line in opened_file:

            # match found so it enters to library page
            if combination in line:
                print("Username and password is: " + line)
                found = True
                controller.show_frame(Library_Page)

        opened_file.close()

        # if match not found it returns info to user
        if found == False:
            tk = Tk()
            tk.geometry("100x100")
            show_msg = Message(tk, text = "Username or password incorrect")
            show_msg.config(bg="lightblue", font=("times",15))
            show_msg.pack() 

        

        # deletes the entries after login button is pressed
        self.username_login_entry.delete(0, END)
        self.password_login_entry.delete(0, END)
    

    def login_success(self):
        # user succesfully logins to the e-library and is moved to library page
        Library_Page()

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
        
        # Register button will run on_register() program that will check input
        register_button = tk.Button(self, text='Submit', height="2", width="20",
        command= lambda: self.on_register(controller))
        register_button.pack(pady=10)

        # Back button returns to homepage
        back_button = tk.Button(self, text='Go back', height="2", width="20",
        command=lambda: controller.show_frame(HomePage))
        back_button.pack(pady=10)

    def on_register(self,controller):
        # This function checks that users input values are valid and if they are
        # it will save them to txt file and return homepage

        # TÄHÄN vois myös tallentaa emailit, puhnro, etu ja suku-nimet johonkin objektiin jonka tiedot nähtäisi sitten profiilissa?? 
        # hankalaa
        
        if self.reg_validation()==True:
            self.save_input()
            controller.show_frame(HomePage)
    

    def save_input(self):
        tk = Tk()
        # get the username and password
        get_username = self.username.get()
        get_password = self.password.get()

        # open file where the data goes
        base_folder = os.path.dirname(__file__)
        information_file_path = os.path.join(base_folder, 'user_information.txt')
        user_file = open(information_file_path, "a+")
        print("File opened.")
        user_file.write(get_username + ":" + get_password + "\n")
        print("Closing file.")
        user_file.close()

        # makes the entries empty
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

        
    def reg_validation(self):
            tk = Tk()
            name = self.username.get()
            pw = self.password.get()
            msg = ''
            its_valid = False  # this is false until username and password are valid
            bg_color = "red"  # background on message is red until it's valid
            
            if len(name) == 0:
                msg = 'Username can\'t be empty'

            elif len(pw) == 0:
                msg = 'Password can\'t be empty'

            else:
                try:
                    if not any(ch.isdigit() for ch in pw):
                        msg = 'Password must have numbers in it'
                    elif len(name) <= 2:
                        msg = 'Username is too short.'
                    elif len(name) > 100:
                        msg = 'Username is too long.'
                    else:
                        msg = 'Registration confirmed!'
                        its_valid = True   # here it changes true and all the input is correct
                        bg_color = "green"
                        
                except Exception as ep:
                    msg = "Error: " +  ep

            # Displays information message to user
            show_msg = Message(tk, text = msg)
            show_msg.config(bg=bg_color, font=("times",15))
            show_msg.pack() 
            return its_valid
            

class Library_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # image label
        bg_label = tk.Label(self, image = img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        text3_label = tk.Label(self, text="Do you wan't to loan books movies or magazines?", bg="white", fg="black", font=('Helvetica', '15', 'bold'))
        text3_label.pack(pady=10,padx=10)

        base_folder = os.path.dirname(__file__)
        
        # Importing images to be used as a buttons
        book_image_path = os.path.join(base_folder, 'book_icon.png')
        self.Book_Image = tk.PhotoImage(file = book_image_path)
        self.Book_Icon = self.Book_Image.subsample(7, 5) # Resizing the image to fit on the button

        movie_image_path = os.path.join(base_folder, 'movie_icon.png')
        self.Movie_Image = tk.PhotoImage(file = movie_image_path)
        self.Movie_Icon = self.Movie_Image.subsample(7, 7)

        magazine_image_path = os.path.join(base_folder, 'magazine_icon.png')
        self.Magazine_Image = tk.PhotoImage(file = magazine_image_path)
        self.Magazine_Icon = self.Magazine_Image.subsample(16, 17)

        Book_Button = tk.Button(self, text = "Books", image = self.Book_Icon, command=lambda: controller.show_frame(BookPage))
        Book_Button.place(x=60, y=80)

        Movie_Button = tk.Button(self, text = "Movies", image = self.Movie_Icon)
        Movie_Button.place(x=235, y=80)

        Magazine_Button = tk.Button(self, text = "Magazines", image = self.Magazine_Icon)
        Magazine_Button.place(x=395, y=80)

        log_out_button = tk.Button(self, text='Log out', height="2", width="20",
        command=lambda: controller.show_frame(HomePage))
        log_out_button.place(x=200, y=330)

class BookPage(tk.Frame):

    # Idea teksti tiedosto jossa kirjat taulukossa ne lisätään jollain for loopilla
    # kirjan kannesta kuvat book_pics kansiossa josta ne otetaan

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # image label
        bg_label = tk.Label(self, image = img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        text3_label = tk.Label(self, text="A selection of books", bg="white", fg="black", font=('Helvetica', '15', 'bold'))
        text3_label.pack(pady=10,padx=10)

        
        # base_folder is path help for finding right files
        base_folder = os.path.dirname(__file__)

        # Let's get into book information text file and change its type from string 
        # to dictionary with ast.literal_eval -tool
        book_info_path = os.path.join(base_folder, 'book_information.txt')
        book_info_file = open(book_info_path, "r")
        book_info_data = book_info_file.read()
        book_info_dict = ast.literal_eval(book_info_data)

         # Register button will run on_register() program that will check input
        test_button = tk.Button(self, text='test', height="2", width="20",
        command= lambda: self.show_books(controller, book_info_dict))
        test_button.pack(pady=10)


        #print(book_info_dict['book2']['photo'])
        #print(base_folder + '\\book_pics\\' + book_info_dict['book2']['photo'])
        #book_cover_path = os.path.join(base_folder + '\\book_pics\\' + book_info_dict['book2']['photo'])
        #self.book_cover = tk.PhotoImage(file = book_cover_path)
        #self.book_cover_img = self.book_cover.subsample(16, 17)

        #Book_Button = tk.Button(self, text = "Books", image = self.book_cover_img, command=lambda: controller.show_frame(Library_Page))
        #Book_Button.place(x=60, y=80)


            
            


        #book_info_file.close()

    def show_books(self,controller,dict_obj):
    
        base_folder = os.path.dirname(__file__)
        for i in dict_obj:
            # display
            print(dict_obj[i].values())



        first_x = 60
        second_y = 100
        photo_paths = []
        
        for key in dict_obj:

            photo_paths.append(dict_obj[key]['photo'])

    
            book_cover_path = os.path.join(base_folder + '\\book_pics\\' + dict_obj[key]['photo'])
            self.book_cover = tk.PhotoImage(file = book_cover_path)
            self.book_cover_img = self.book_cover.subsample(16, 17)


            Book_Button = tk.Button(self, text = "Book", image = self.book_cover_img, command=lambda: controller.show_frame(Library_Page))
            Book_Button.place(x=first_x, y=second_y)
            first_x= first_x + 100

        
        
        

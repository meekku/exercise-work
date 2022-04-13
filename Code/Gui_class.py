import tkinter as tk
from tkinter import *
import os
from colorama import Back
import Book_class
import ast
import User_class

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
        for F in (HomePage, Page_Login, Page_Register, Library_Page, BookPage, ProfilePage):
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
        # Here we see if user's input
        # matches information ar user_information.txt
        # if yes then user can log in and sees librarypage

        # get the username and the password
        verify_username = self.username_login.get()
        verify_password = self.password_login.get()
        combination = verify_username + ":" + verify_password # this is what we are looking for from the file
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
                self.current_user(verify_username)
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
    
    def current_user(self, username):
        # this is for profile to find which user information to show
        print(username)
        # open file where the data goes
        base_folder = os.path.dirname(__file__)
        f_path = os.path.join(base_folder, 'current_user.txt')
        open_file = open(f_path, "a+")
        open_file.write(username)
        open_file.close()


class Page_Register(tk.Frame):
    # in this class we ask user's information
    # check that it is valid and save it for 
    # further purposes
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # image label
        bg_label = tk.Label(self, image = img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # header
        self.header_label = tk.Label(self, text="E-Library Register", bg="white", fg="black", font=('Helvetica', '32', 'bold'))
        self.header_label.pack(pady=10,padx=10)

        # let's initialize all variables
        self.username = StringVar()
        self.password = StringVar()
        self.first_name = StringVar()
        self.last_name = StringVar()
        self.phone = StringVar()
        self.email = StringVar()

        # Set label for user's instruction
        instruction_label = tk.Label(self, text="Please enter details below", bg="white", fg="black", 
        font=('Helvetica', '16'))
        instruction_label.pack(pady=8)

        # Information text label
        info_label = tk.Label(self, text="Username: \n\n Password: \n\n First name: \n\n Last name: \n\n Phonenumber: \n\n E-mail: ", bg="white", fg="black", font=('Helvetica', '8'))
        info_label.place(x=158, y=131)

        # Set username entry
        self.username_entry = tk.Entry(self, textvariable=self.username, bg="white", fg="black")
        self.username_entry.pack(pady=9)

        # Set password entry
        self.password_entry = tk.Entry(self, textvariable=self.password, show='*', bg="white", fg="black")
        self.password_entry.pack()

        # Set first name entry
        self.first_name_entry = tk.Entry(self, textvariable=self.first_name, bg="white", fg="black")
        self.first_name_entry.pack(pady=9)

        # Set last name entry
        self.last_name_entry = tk.Entry(self, textvariable=self.last_name, bg="white", fg="black")
        self.last_name_entry.pack()

        # Set phonenumber entry
        self.phone_entry = tk.Entry(self, textvariable=self.phone, bg="white", fg="black")
        self.phone_entry.pack(pady=9)

        # Set email entry
        self.email_entry = tk.Entry(self, textvariable=self.email, bg="white", fg="black")
        self.email_entry.pack()
        
        # Register button will run on_register() program that will check input
        register_button = tk.Button(self, text='Submit', height="2", width="15",
        command= lambda: self.on_register(controller))
        register_button.pack(pady=5)

        # Back button returns to homepage
        back_button = tk.Button(self, text='Go back', height="2", width="20",
        command=lambda: controller.show_frame(HomePage))
        back_button.pack(pady=5)

    def on_register(self,controller):
        # This function first runs reg_validation() which
        # checks that users input values are valid, if they are
        # it will run save_input() function that will save
        # information. After that it will go to Homepage and clear entries

        if self.reg_validation()==True:
            # save_input function saves password and username for login purposes
            self.save_input()

            # Back to home page
            controller.show_frame(HomePage)

            # makes the entries empty
            self.first_name_entry.delete(0, END)
            self.last_name_entry.delete(0, END)
            self.phone_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)

    def reg_validation(self):
        # this function checks that users input
        # is valid for registration
            tk = Tk()
            name = self.username.get() 
            pw = self.password.get()
            msg = ''
            its_valid = False  # this is false until username and password are valid
            bg_color = "red"  # background on message is red until it's valid
            found = True

            # These lines are for looking that username is not taken already
            base_folder = os.path.dirname(__file__)
            usernames_file_path = os.path.join(base_folder, 'user_information.txt')
            usernames_file = open(usernames_file_path, "r")
            for line in usernames_file:
                if name in line:
                    found = False
                    msg = 'Username is already taken'

            # These lines will run if username is not taken
            if found == True:
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

    def save_input(self):
        # this functions saves users input to two files
        # user_information.txt will contain username and password
        # for login purposes and profile_info.txt contains 
        # all asked information except password

        # get the username and password
        get_username = self.username.get()
        get_password = self.password.get()

        # Here we save password and username only
        # open file where the data goes
        base_folder = os.path.dirname(__file__)
        information_file_path = os.path.join(base_folder, 'user_information.txt')
        user_file = open(information_file_path, "a+")
        print("File opened.")
        user_file.write(get_username + ":" + get_password + "\n")
        print("Closing file.")
        user_file.close()

        # Here we save all information except password
        # open file where the data goes
        users_file_path = os.path.join(base_folder, 'profile_info.txt')
        users_file = open(users_file_path, "a+")
        users_file.write(self.username.get() + "," + self.first_name.get()+ "," + self.last_name.get()+ "," + self.phone.get() + "," +self.email.get() + "\n")
        users_file.close()


class Library_Page(tk.Frame):
    # This is first screen that we see after login
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # image label
        bg_label = tk.Label(self, image = img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # header label
        header_label = tk.Label(self, text="Do you wan't to loan books movies or magazines?", bg="white", fg="black", font=('Helvetica', '15', 'bold'))
        header_label.pack(pady=10,padx=10)

        # base folder to help find right file
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

        Profile_Button = tk.Button(self, text = "Your profile", height="2", width="20", command=lambda: controller.show_frame(ProfilePage))
        Profile_Button.place(x=220,y=240)

        log_out_button = tk.Button(self, text='Log out', height="2", width="20",
        command=lambda: self.clear_current_user_file(controller))
        log_out_button.place(x=220, y=300)

    def clear_current_user_file(self, controller):
    
        base_folder = os.path.dirname(__file__)
        f_path = os.path.join(base_folder, 'current_user.txt')
        open_file = open(f_path, "w").close()
        controller.show_frame(HomePage)

class BookPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # image label
        bg_label = tk.Label(self, image = img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # header
        header_label = tk.Label(self, text="A selection of books", bg="white", fg="black", font=('Helvetica', '15', 'bold'))
        header_label.pack(pady=10,padx=10)

        # our books as an objects so we can use for loop to
        # show their information
        book1 = Book_class.Book("I hate my life 3", "Fantasy", "3002", "Myself", "12.4.2022", "book1.png")
        book2 = Book_class.Book("Students lost motivation", "Horror", "301", "Bookkers", "23.3.2003", "book2.png")
        book3 = Book_class.Book("Best bible", "Nonfiction", "20", "God", "30.2.1999", "book3.png")
        books = [book1, book2, book3]

        # buttons for loaning spesific book
        loan1_button = tk.Button(self, text = "Loan", height = 2, width= 5, command=lambda: self.loan(book1))
        loan1_button.place(x=100, y=90)
        loan2_button = tk.Button(self, text = "Loan", height = 2, width= 5, command=lambda: self.loan(book2))
        loan2_button.place(x=100, y=190)
        loan3_button = tk.Button(self, text = "Loan", height = 2, width= 5, command=lambda: self.loan(book3))
        loan3_button.place(x=100, y=290)

        for book in books:
            # text labels which contains all three book's information
            text_label = tk.Label(self, text=book, bg="white", fg="black", font=('Helvetica', '10', 'bold'))
            text_label.pack(pady=10,padx=10)

        # Now let's add images for books
        # base_folder is path help for finding right files
        base_folder = os.path.dirname(__file__)

        # book1 -object's image
        book1_cover_path = os.path.join(base_folder + '\\book_pics\\' + book1.get_photo())
        self.book1_cover = tk.PhotoImage(file = book1_cover_path)
        self.book1_cover_img = self.book1_cover.subsample(2, 2)
        book1_img_label = tk.Label(self, image = self.book1_cover_img)
        book1_img_label.place(x=450, y=70)

        # book2 -object's image
        book2_cover_path = os.path.join(base_folder + '\\book_pics\\' + book2.get_photo())
        self.book2_cover = tk.PhotoImage(file = book2_cover_path)
        self.book2_cover_img = self.book2_cover.subsample(2, 2)
        book2_img_label = tk.Label(self, image = self.book2_cover_img)
        book2_img_label.place(x=455, y=175)

        # book3 -object's image
        book3_cover_path = os.path.join(base_folder + '\\book_pics\\' + book3.get_photo())
        self.book3_cover = tk.PhotoImage(file = book3_cover_path)
        self.book3_cover_img = self.book3_cover.subsample(2, 2)
        book3_img_label = tk.Label(self, image = self.book3_cover_img)
        book3_img_label.place(x=450, y=280)

        # return button
        return_button = tk.Button(self, text='<<', height="1", width="10",
        command=lambda: controller.show_frame(Library_Page))
        return_button.place(x=2, y=2)
    
    def loan(self,book):
        # ideaa ei ole jotenkin lainat pitäisi saada tehtyä , että ne näkyisi profiilissa
        print(book)

        
class ProfilePage(tk.Frame):

    # Idea Profiili sivu, jossa näkee omat tiedot ja lainat sillä käyttäjällä

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # image label
        bg_label = tk.Label(self, image = img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # initializing current_user, this is not a must
        current_user = ""

        # basefolder file to help searching right files
        base_folder = os.path.dirname(__file__)

        # this file shows what user is now login
        f_path = os.path.join(base_folder, 'current_user.txt')
        open_file = open(f_path, "r")
        current_username = open_file.readline()

        # we will find user's information
        # from profile_info.txt file where is all users 
        # registrationg informations saved
        usernames_file_path = os.path.join(base_folder, 'profile_info.txt')
        usernames_file = open(usernames_file_path).readlines()

        # this for loop finds line for username which
        # is login at the moment and creates object of that user info
        for line in usernames_file:
            if current_username in line:
                row = line.split(',')
                user_name, fname, lname, phone, email = [i.strip() for i in row]
                current_user = User_class.User(user_name, fname, lname, phone, email)
            

        # header
        header_label = tk.Label(self, text="Your profile", bg="white", fg="black", font=('Helvetica', '15', 'bold'))
        header_label.pack(pady=10,padx=10)
 
        # profile text information
        profile_text_label = tk.Label(self, text=current_user, bg="white", fg="black", font=('Helvetica', '10', 'bold'))
        profile_text_label.pack(pady=10,padx=10)

        # button for returning
        return_button = tk.Button(self, text='<<', height="1", width="10",
        command=lambda: controller.show_frame(Library_Page))
        return_button.place(x=2, y=2)






        
        
# File-name: main.py
# Author: Melina Kamunen and Nea Träskman
# Description: 


import User_class
import Loan_class
from tkinter import *


def main():


    library = User_class.User("Nea", "Träskman")


    print(library)



def main_login_screen():

    main_screen = Tk() # creating the GUI
    main_screen.geometry("300x250") # setting the size of the GUI window
    main_screen.title("Library - Login") # title of the GUI window

    #creating the form label
    Label(text="Login or Register", bg="gray", width="300", height="2", font=("Calibri", 12)).pack()
    Label(text="").pack()

    # creating the login button
    Button(text="Login", height="2", width="30").pack()
    Label(text="").pack()

    # creating the register button
    Button(text="Register", height="2", width="30").pack()

    main_screen.mainloop() # starts the GUI

main_login_screen()



if __name__ == "__main__":
    main()
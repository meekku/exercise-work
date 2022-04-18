# File-name: main.py
# Author: Melina Kamunen and Nea Träskman
# Description: main.py acts as a startup file to open the program code and GUI interface about the e-library.In e-library you can create users that can log in to the service, where you can borrow books, movies and magazines. The program also gives you access to see and return your own loans, and look at your profile.


import Gui_class

def main():
    

    app = Gui_class.App()
    app.mainloop()


if __name__ == "__main__":
    main()
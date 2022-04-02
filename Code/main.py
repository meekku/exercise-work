# File-name: main.py
# Author: Melina Kamunen and Nea Träskman
# Description: 

import User_class
import Loan_class
import Gui_class

def main():
    
    library = User_class.User("Nea", "Träskman")
    print(library)

    app = Gui_class.App()
    app.mainloop()


if __name__ == "__main__":
    main()
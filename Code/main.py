# File-name: main.py
# Author: Melina Kamunen and Nea Träskman
# Description: 

import User_class
import Loan_class
import Gui_class

def main():
    
    user2 = User_class.User("Meekku","Melina","Kamunen","0400299293","mee@")
    user2.add_loan("12.4.2022","22.4.2022","Book loser")
    user2.add_loan("12.3.2022","12.4.2022","Secret book")
    print(user2)

    app = Gui_class.App()
    app.mainloop()


if __name__ == "__main__":
    main()
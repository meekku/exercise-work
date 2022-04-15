# File-name: main.py
# Author: Melina Kamunen and Nea Träskman
# Description: main.py acts as a startup file to open the program code and GUI interface about the e-library.In e-library you can create users that can log in to the service, where you can borrow books, movies and magazines. The program also gives you access to see and return your own loans, and look at your profile.


import Gui_class

def main():
    
    # PUUTTUU:

    # 1. Ei ole vielä magazine tai movie sivuja tai lainoja yhdistetty luokkiin :_:
    # 2. Ohjelman suoritukseen tarvitsee luoda tyhjiä tekstitiedostoja:
    #  - current_user.txt
    #  - loan_and_user.txt
    #  - loans.txt
    #  - profile_info.txt
    #  - user_information.txt
    #  Nää teksti tiedostot toimivat vähän kuin tietokantana, että tallentaa käyttäjien juttuja
    # 3. Testausta pitäis myös jaksaa, koska ongelmia uskottavasti löytyyy
    # 4. lopuksi jos on aikaa niin koristellaan 

    app = Gui_class.App()
    app.mainloop()


if __name__ == "__main__":
    main()
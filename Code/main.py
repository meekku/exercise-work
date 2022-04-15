# File-name: main.py
# Author: Melina Kamunen and Nea Träskman
# Description: 


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

    app = Gui_class.App()
    app.mainloop()


if __name__ == "__main__":
    main()
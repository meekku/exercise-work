# File-name: main.py
# Author: Melina Kamunen and Nea Träskman
# Description: 

import User_class
import Loan_class
import Gui_class

def main():
    
    # PUUTTUU:
    # 1. Profiili teksti muodostuu automaattisesti kun ajaa koodin. Ongelma on että se kerää käyttäjä nimen current_user.txt tiedostosta
    # ja se on tyhjä yleensä ajon aikana joten profiili teksti ei päivity ja voi olla aikaisemman käyttäjän 
    # yks ratkasu ois tehä profiili sivulle button joka näyttää profiili tekstin
    # 2. Ei ole vielä magazine tai movie sivuja tai lainoja yhdistetty luokkiin :_:
    # 3. Ohjelman suoritukseen tarvitsee luoda tyhjiä tekstitiedostoja:
    #  - current_user.txt
    #  - loan_and_user.txt
    #  - loans.txt
    #  - profile_info.txt
    #  - user_information.txt
    #  Nää teksti tiedostot toimivat vähän kuin tietokantana, että tallentaa käyttäjien juttuja

    app = Gui_class.App()
    app.mainloop()


if __name__ == "__main__":
    main()
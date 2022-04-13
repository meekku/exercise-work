# File-name: User_class.py
# Author: Melina Kamunen and Nea Träskman
# Description: User_class.py is class for creating spesific users to library program
import Loan_class

class User():

    def __init__(self,user_name , first_name, last_name, phonenumber, email):
        self.__user_name = user_name
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phonenumber = phonenumber
        self.__email = email
        self.__loans = []
    
    def __str__(self):
        st= "Username: " + str(self.get_user_name()) + "\nName: " + str(self.get_first_name()) + " " + str(self.get_last_name()) + "\n Phone: " + str(self.get_phonenumber()) + "\n E-mail: " + str(self.get_email())

        if (len(self.__loans)>0):
            st += ", \n loans: "
            for i in self.__loans:
                st += str(i) + ", "
                
        return st
    
# Setters for user's properties
    def set_user_name(self, new_user_name):
        self.__user_name = new_user_name
    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name
    def set_last_name(self, new_last_name):
        self.__last_name = new_last_name
    def set_phonenumber(self, new_phonenumber):
        self.__phonenumber = new_phonenumber
    def set_email(self, new_email):
        self.__email = new_email 

# Getters for user's properties
    def get_user_name(self):
        return self.__user_name
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    def get_phonenumber(self):
        return self.__phonenumber
    def get_email(self):
        return self.__email


    def add_loan(self,loan_id, start, end, name, genre="-", pages="-", producer="-",release_date="-", photo="-"):
        new_loan = Loan_class.Loan(start,end,name, genre, pages, producer, release_date, photo)
        new_loan.set_loan_id(loan_id)
        self.__loans.append(new_loan)
    


    def return_loan(self):
        self.__loans.pop()
     
    def show_loans(self):
        for i in self.__loans:
            print(i)

    
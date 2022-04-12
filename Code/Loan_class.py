# File-name: Loan_class.py
# Author: Nea Träskman and Melina Kamunen
# Description: 
import itertools
import Book_class
import User_class

class Loan():

    id_counter = itertools.count()
    def __init__(self, start_date, end_date, name, user_name, first_name, last_name):
        self.__loan_id =  next(Loan.id_counter) +1
        self.__start_date = start_date
        self.__end_date = end_date
        self.__invoice_amount = 0 # at the beginning

        Book_class.Book.__init__(self, name)
        User_class.User.__init__(self,user_name, first_name, last_name)
    
    def __str__(self):
        st = "Loan" + str(self.get_loan_id()) + ", " + Book_class.Book.get_name() + " has been loaned  " + str(self.get_start_date()) + " \n by:  " + User_class.User.get_first_name() + " " +  User_class.User.get_last_name() + "\n Expiration date is: " + str(self.get_end_date()) + " and invoice amount: " + str(self.get_invoice_amount())

        return st

# Setters for loan's properties
    def set_start_date(self, new_start_date):
        self.__start_date = new_start_date
    def set_end_date(self, new_end_date):
        self.__end_date = new_end_date


# Getters for loan's properties
    def get_loand_id(self):
        return self.__loan_id
    def get_start_date(self):
        return self.__start_date
    def get_end_date(self):
        return self.__end_date
    def get_invoice_amount(self):
        return str(self.__invoice_amount)

# functions for adding and reducing invoice
    def add_invoice(self, more_invoice):
        self.__invoice_amount += more_invoice
    def pay_invoice(self, less_invoice):
        self.__invoice_amount -= less_invoice


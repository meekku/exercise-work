# File-name: Loan_class.py
# Author: Nea Träskman and Melina Kamunen
# Description: 
import itertools
import Book_class
import User_class

class Loan():

    id_counter = itertools.count()
    def __init__(self, start_date, end_date, name, genre, pages, producer, release_date, photo):
        self.__loan_id =  next(Loan.id_counter) +1
        self.__start_date = start_date
        self.__end_date = end_date
        self.__invoice_amount = 0 # at the beginning
        self.__loan_active = True

        Book_class.Book.__init__(self, name, genre, pages, producer, release_date, photo)
    
    def __str__(self):
        st = "Loan" + str(self.get_loan_id()) + ", Loan time:" + str(self.get_start_date()) + " -  " + str(self.get_end_date()) + " and invoice amount: " + str(self.get_invoice_amount())

        return st

# Setters for loan's properties
    def set_start_date(self, new_start_date):
        self.__start_date = new_start_date
    def set_end_date(self, new_end_date):
        self.__end_date = new_end_date


# Getters for loan's properties
    def get_loan_id(self):
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
        self.__loan_active = False


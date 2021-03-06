# File-name: Loan_class.py
# Author: Nea Träskman and Melina Kamunen
# Description: Loan class is for creating loans about book class

import Book_class
import random
class Loan(Book_class.Book):

    
    def __init__(self, start_date, end_date, name, genre, pages, producer, release_date, photo):
        self.__loan_id =  random.randint(0,99999)*123456
        self.__start_date = start_date
        self.__end_date = end_date

        Book_class.Book.__init__(self, name, genre, pages, producer, release_date, photo)
    
    def __str__(self):
        st = Book_class.Book.__str__(self)
        st += "\nLoan ID: " + str(self.get_loan_id()) + "\nLoan time:" + str(self.get_start_date()) + " -  " + str(self.get_end_date()) + "\n"
        return st

# Setters for loan's properties
    def set_start_date(self, new_start_date):
        self.__start_date = new_start_date
    def set_end_date(self, new_end_date):
        self.__end_date = new_end_date
    def set_loan_id(self, new_loan_id):
        self.__loan_id= new_loan_id


# Getters for loan's properties
    def get_loan_id(self):
        return str(self.__loan_id)
    def get_start_date(self):
        return self.__start_date
    def get_end_date(self):
        return self.__end_date





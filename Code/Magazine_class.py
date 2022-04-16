# File-name: Magazine_class.py
# Author: Nea Träskman and Melina Kamunen
# Description: Magazine_class.py is for creating magazine objects

class Magazine():

    def __init__(self, name, pages, release_date, photo):
        self.__name = name
        self.__pages = pages
        self.__release_date = release_date
        self.__photo = photo

    
    def __str__(self):
        st= "Name: " + str(self.get_name()) + "\n Pages: " + str(self.get_pages()) + "\n Release date: " + str(self.get_release_date())
        return st
    
# Setters for magazine's properties
    def set_name(self, new_name):
        self.__name = new_name
    def set_pages(self, new_pages):
        self.__pages = new_pages
    def set_release_date(self, new_release_date):
        self.__release_date = new_release_date
    def set_photo(self, new_photo):
        self.__photo = new_photo

# Getters for magazine's properties
    def get_name(self):
        return self.__name
    def get_pages(self):
        return self.__pages
    def get_release_date(self):
        return self.__release_date
    def get_photo(self):
        return self.__photo
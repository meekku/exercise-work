# File-name: Movie_class.py
# Author: Nea Träskman and Melina Kamunen
# Description: Movie_class.py is for creating movie objects

class Movie():

    def __init__(self, name, genre, producer, release_date, photo):
        self.__name = name
        self.__genre = genre
        self.__producer = producer
        self.__release_date = release_date
        self.__photo = photo

    
    def __str__(self):
        st= "Name: " + str(self.get_name()) + "\n Genre: " + str(self.get_genre()) + "\n Producer: " + str(self.get_producer()) + "\n Release date: " + str(self.get_release_date())
        return st
    
# Setters for movie's properties
    def set_name(self, new_name):
        self.__name = new_name
    def set_genre(self, new_genre):
        self.__genre = new_genre
    def set_producer(self, new_producer):
        self.__producer = new_producer
    def set_release_date(self, new_release_date):
        self.__release_date = new_release_date
    def set_photo(self, new_photo):
        self.__photo = new_photo

# Getters for movie's properties
    def get_name(self):
        return self.__name
    def get_genre(self):
        return self.__genre
    def get_producer(self):
        return self.__producer
    def get_release_date(self):
        return self.__release_date
    def get_photo(self):
        return self.__photo
# File-name: User_class.py
# Author: Melina Kamunen and Nea Träskman
# Description: 


class User():


    def __init__(self, UserFirstName, UserLastName):
        self.__UserFirstName = UserFirstName
        self.__UserLastName = UserLastName
    
    def __str__(self):
        return "Name: " + str(self.__UserFirstName) + " " + str(self.__UserLastName)
    
# Set and Get for User's first name
    def set_UserFirstName(self, UserFirstName):
        self.__UserFirstName = UserFirstName
    def get_UserFirstName(self):
        return self.__UserFirstName

# Set and Get for User's last name
    def set_UserLastName(self, UserLastName):
        self.__UserLastName = UserLastName
    def get_UserLastName(self):
        return self.__UserLastName
class Personne:
    def __init__(self, firstname, lastname):
        self.__firstname = firstname
        self.__lastname = lastname

    def get_firstname(self):
        return self.__firstname
    def get_lastname(self):
        return self.__lastname

    def set_firstname(self,firstname):
        self.__firstname= firstname

    def set_lastname(self,lastname):
        self.__lastname = lastname
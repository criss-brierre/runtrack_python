class Person:
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
    
    def se_presenter(self):
        return print("Bonjour ! Je m'appelle "+ self.__firstname +" "+ self.__lastname +".")

person_1 = Person("Criss","Brierre")
person_2 = Person("Alice","Torniole")
person_3 = Person("Gerard","Routier")

person_1.se_presenter()
person_2.se_presenter()
person_3.se_presenter()

print(person_3.get_lastname())

person_2.set_firstname("Pauline")

print(person_2.get_firstname())

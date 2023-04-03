import sys
sys.path.insert(0, '../classes')

class Livre:
    def __init__(self, titre, firstname, lastname):
        self.__titre = titre
        from auteur import Auteur
        self.auteur = Auteur(firstname,lastname)

    def get_title(self):
        print("Titre : " + self.__titre)

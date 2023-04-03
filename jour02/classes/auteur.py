import sys
sys.path.insert(0, '../classes')

from personne import Personne
from livre import Livre

class Auteur(Personne):
    def __init__(self, firstname, lastname):
        super().__init__(firstname,lastname) 

        self.oeuvres = {"Livre 1": 10, "Livre 2": 5}
    
    def lister_oeuvre(self):
        return self.oeuvres

    
    def ecrire_livre(self,title):
        livre = Livre(title,self.get_firstname,self.get_lastname)
        self.oeuvres[title] = 3

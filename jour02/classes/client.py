import sys
sys.path.insert(0, '../classes')

from personne import Personne

class Client(Personne):
    def __init__(self, firstname, lastname):
        super().__init__(firstname,lastname) 
        self.collection = {}

    def inventaire(self):
        print("Livres en possession de", self.get_firstname(), self.get_lastname(), ":")
        for livre, quantite in self.collection.items():
            print(livre, "(", quantite, ")")

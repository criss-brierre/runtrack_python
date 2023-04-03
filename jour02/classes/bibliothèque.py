class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = {}

    def acheterLivre(self, auteur, titre, quantite):
        if titre in auteur.oeuvres:
            if titre in self.catalogue:
                self.catalogue[titre] += quantite
            else:
                self.catalogue[titre] = quantite

    def inventaire(self):
        print("Catalogue de la bibliothèque", self.nom, ":")
        for livre, quantite in self.catalogue.items():
            print(livre, "(", quantite, ")")

    def louer(self, client, titre):
        if titre in self.catalogue and self.catalogue[titre] > 0:
            if titre in client.collection:
                client.collection[titre] += 1
            else:
                client.collection[titre] = 1
            self.catalogue[titre] -= 1

    def rendreLivres(self, client):
        for livre, quantite in client.collection.items():
            if livre in self.catalogue:
                self.catalogue[livre] += quantite
            else:
                self.catalogue[livre] = quantite
        client.collection = {}

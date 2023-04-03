import sys
sys.path.insert(0, '../classes')

from auteur import Auteur
from client import Client
from bibliothèque import Bibliotheque

auteur = Auteur("Toto","Bernard")
auteur.lister_oeuvre()
bibliotheque = Bibliotheque("Bibliothèque municipale")
client = Client("Dupont", "Jean")
bibliotheque.acheterLivre(auteur, "Livre 1", 8)
bibliotheque.acheterLivre(auteur, "Livre 2", 3)
bibliotheque.inventaire()
client.inventaire()
bibliotheque.louer(client, "Livre 1")
bibliotheque.inventaire()
client.inventaire()
bibliotheque.rendreLivres(client)
bibliotheque.inventaire()
client.inventaire()
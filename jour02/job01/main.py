import sys
sys.path.insert(0, '../classes')

from auteur import Auteur

Auteur = Auteur("Criss","Brierre")

Auteur.ecrire_livre("Harry Potter")
Auteur.ecrire_livre("Livre n'1")
Auteur.ecrire_livre("Livre n'2")
Auteur.ecrire_livre("Le meilleur dans le pathé c'est le gras")

oeuvre_list = Auteur.lister_oeuvre()

for livre in oeuvre_list:
    print(livre)
    

    
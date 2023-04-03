import string

word_count = 0

# Parcours du fichier "data.txt"
with open("../txt/data.txt", "r") as data_file:
    for line in data_file:
        # Suppression des caractères spéciaux et découpage en mots
        words = line.strip().translate(str.maketrans('', '', string.punctuation)).split()
        # Incrémentation du compteur de mots
        word_count += len(words)

# Affichage du résultat
print(f"Nombre de mots : {word_count}")
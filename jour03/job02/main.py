import string
n = int(input("Entrez un nombre entier : "))

n_word_count = 0

with open("../txt/data.txt", "r") as data_file:
    for line in data_file:
        # Suppression des caractères spéciaux et découpage en mots
        words = line.strip().translate(str.maketrans('', '', string.punctuation)).split()
        # Comptage des mots de taille n
        for word in words:
            if len(word) == n:
                n_word_count += 1

print(f"Nombre de mots de taille {n} : {n_word_count}")
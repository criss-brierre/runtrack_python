import matplotlib.pyplot as plt

with open("../txt/data.txt", "r") as f:
    word_count = {}
    for line in f:
        words = line.split()
        for word in words:
            word_length = len(word)
            if word_length in word_count:
                word_count[word_length] += 1
            else:
                word_count[word_length] = 1

    total_words = sum(word_count.values())
    for length, count in word_count.items():
        word_count[length] = count/total_words * 100

    plt.bar(word_count.keys(), word_count.values())
    plt.xlabel('Taille des mots')
    plt.ylabel('Pourcentage d\'apparition')
    plt.title('Histogramme de la taille des mots dans data.txt')
    plt.show()
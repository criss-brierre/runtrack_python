import re
import random
import matplotlib.pyplot as plt

with open("../txt/data.txt", "r") as f:
    num_words = []
    for line in f:
        line = line.strip()
        words = re.findall(r'\b\w+\b', line)
        num_words.append(len(words))

plt.hist(num_words, bins=range(max(num_words)+1))
plt.title("Histogramme du nombre de mots par phrase")
plt.xlabel("Nombre de mots")
plt.ylabel("Nombre de phrases")
plt.show()

with open("../txt/data.txt", "r") as f:
    stats = {}
    for line in f:
        line = line.strip()
        words = re.findall(r'\b\w+\b', line)
        num_words = len(words)
        if num_words not in stats:
            stats[num_words] = []
        for word in words:
            stats[num_words].append(word)

    for i in range(5):
        num_words = random.choice(list(stats.keys()))
        words = [random.choice(stats[num_words]) for j in range(num_words)]
        sentence = " ".join(words) + "."
        print(sentence)
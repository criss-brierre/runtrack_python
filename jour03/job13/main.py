import matplotlib.pyplot as plt

filename = "../txt/data.txt"
counts = {}

with open(filename, 'r') as f:
    for line in f:
        for i in range(len(line)-1):
            if line[i].isalpha() and line[i+1].isalpha():
                letter = line[i].lower()
                next_letter = line[i+1].lower()
                if letter not in counts:
                    counts[letter] = {}
                counts[letter][next_letter] = counts[letter].get(next_letter, 0) + 1

for letter in counts:
    total = sum(counts[letter].values())
    percentages = {k: v/total*100 for k, v in counts[letter].items()}
    plt.plot(percentages.keys(), percentages.values(), label=letter)

plt.legend()
plt.xlabel("Lettre suivante")
plt.ylabel("Pourcentage d'apparition")
plt.show()
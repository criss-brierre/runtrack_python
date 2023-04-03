import matplotlib.pyplot as plt

filename = "../txt/data.txt"
counts = {}

with open(filename, 'r') as f:
    for line in f:
        words = line.strip().split()
        for word in words:
            if word[0].isalpha():
                letter = word[0].lower()
                counts[letter] = counts.get(letter, 0) + 1

total = sum(counts.values())
percentages = {k: v/total*100 for k, v in counts.items()}

fig, ax = plt.subplots(figsize=(12,6))
ax.bar(percentages.keys(), percentages.values())
ax.set_xlabel("Lettre en début de mot")
ax.set_ylabel("Pourcentage de présence")
plt.show()
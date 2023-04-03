extensions = [".com", ".net", ".org", ".fr", ".uk"]

counts = {ext: 0 for ext in extensions}

with open("../txt/domains.xml", "r") as domains_file:
    for line in domains_file:
        for ext in extensions:
            if ext in line:
                counts[ext] += 1

for ext, count in counts.items():
    print(f"{ext} : {count}")
input_string = input("Entrez une chaîne de caractères : ")

with open("../txt/output.txt", "w") as output_file:
    output_file.write(input_string)

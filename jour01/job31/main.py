import re
def AlphabeticWord():
    # Verifie si l'input donnée par l'utilisateur est bien sans maj / espace / caractère special
    regex = "^[a-z]+$"
    str_word = ""
    while True:
        str_word = input("Veuillez entrer une chaîne de caractères : ")
        if re.match(regex, str_word):
            break
        else:
            print("La chaîne de caractères ne doit contenir que les lettres de l'alphabet en minuscule.")

    # Remplie l'array avec les lettres de l'alphabet
    alphabetic_array = []

    for i in range(ord('a'), ord('z')+1):
        alphabetic_array.append(chr(i))

    temp_array_index = []

    #Stocke l'index des lettres de l'alphabet pour pouvoir leur donner un "poid"

    for i in range(len(str_word)):
        temp_array_index.append(alphabetic_array.index(str_word[i]))
    
    # trie pour que le mot soit le plus proche possible, dans l’ordre alphabétique, du mot original 

    for i in range(len(temp_array_index) - 1, -1, -1):
            
        if(temp_array_index[i] > temp_array_index[i - 1] and i > -1):
            temp_value = temp_array_index[i]
            temp_array_index[i] = temp_array_index[i - 1]
            temp_array_index[i - 1] = temp_value
            break

    #met le tout dans une string pour l'afficher à la fin
    str_final= ""
    for i in range(len(temp_array_index)):
        str_final += alphabetic_array[temp_array_index[i]]

    print(str_final)


AlphabeticWord()

import requests
import json 

def get_name_of_all_pokemon():
    res = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')
    response = json.loads(res.text)
    temp_array = []
    for pokemon in response['results']:
        temp_array.append(pokemon['name'])
    return temp_array

    

pokemon_list = get_name_of_all_pokemon()

with open("../txt/data.txt", "r") as f:
    for line in f:
        words = line.split()
        for word in words:
            if word in pokemon_list:
                print("Le Pokémon anglais trouvé est :", word)
                break
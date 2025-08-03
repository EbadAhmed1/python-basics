
# Connecting an API 

import requests

base_url = "https://pokeapi.co/api/v2"  

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"  
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data for {name}. Status code: {response.status_code}")
        return None  

pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Pokémon ID: {pokemon_info['id']}")  
   
    print(f"Name: {pokemon_info['name']}")
    print(f"Height: {pokemon_info['height']} decimeters")
    print(f"Weight: {pokemon_info['weight']} hectograms")
    print(f"Types: {', '.join([t['type']['name'] for t in pokemon_info['types']])}")
else:
    print("No Pokémon data to display")
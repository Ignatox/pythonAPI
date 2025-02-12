import requests

URL = "https://pokeapi.co/api/v2/pokemon/"

pokemon = input("Escribe un pokemon: ")

response = requests.get(URL + pokemon)

datos = response.json()

print(f"Movimientos de ---- {pokemon}")
for move in datos["moves"]:
    print(move["move"]["name"])
    
print(f"Tipo de pokemon: ")    
for type in datos["types"]:
    print(type["type"]["name"])



import requests

response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons', json={
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers={"trainer_token":"8b65caa7b10c69e4f490acaa43e8b36d", "Content-Type":"application/json"})

print(response.text)

response_put = requests.put(url='https://api.pokemonbattle.me:9104/pokemons', json={
    "pokemon_id": "11393",
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers={"trainer_token":"8b65caa7b10c69e4f490acaa43e8b36d", "Content-Type":"application/json"})

print(response_put.text)


response_poimat = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball', json={
    "pokemon_id": "11393"
}, headers={"trainer_token":"8b65caa7b10c69e4f490acaa43e8b36d", "Content-Type":"application/json"})

print(response_poimat.text)
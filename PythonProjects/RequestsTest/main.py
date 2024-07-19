import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '375a2be572cbe5bd5cfaf2de190b2bde'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_edit_name = {
    "pokemon_id": "44237",
    "name": "Pomelo",
    "photo_id": 6
}

body_add_pokeball = {
    "pokemon_id": "44237"
}


'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_edit_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_edit_name)
print(response_edit_name.text)'''

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)
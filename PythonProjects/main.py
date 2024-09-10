import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5d16a48395c453f226fb11151658003a'
HEADER = {'Content-Type' : 'application/json'}
body_registration = {
    "trainer_token": "токен_из_бота_котика",
    "email": "german@dolnikov.ru",
    "password": "Iloveqa1"
}

response = requests.post(url = f'{URL}/trainers/reg' , headers = HEADER , json = body_registration)
print(response)




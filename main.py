from dotenv import load_dotenv
import os
import requests
import spotipy

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

print(client_id, client_secret)

def song_search(ingredient):
# Register to get an APP ID and key https://developer.edamam.com/
    app_id = ''
    app_key = ''
    result = requests.get('https://developer.spotify.com/documentation/web-api/'.format(ingredient, app_id, app_key))   
    data = result.json()
    return data['hits']
def run():
    ingredient = input('Enter an ingredient: ')
    results = song_search(ingredient)
    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['uri'])
    print()
run()
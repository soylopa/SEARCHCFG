import base64
from requests import post, get
import json

client_id = 'c1fb38329c7e43be8ad7d9887649a609'
client_secret = 'c40e33e17f5f4332a3ab200a340980b9'

search_artist= input('Tell me who: ')
replace_string = search_artist.replace(' ', '%20')
    
def get_token():
    auth_string = str(client_id) + ":" + str(client_secret) #authorisation string+concatenation
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8") #turn into str - request sent to acc service API, url follows
    url = "https://accounts.spotify.com/api/token"
    headers = { #to send auth data + sending back the token we need
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded" #usually there app json, but using copypasted type
    }
    data = {"grant_type": "client_credentials"}
    #after having URL, headers & data, formulate request
    result = post(url, headers=headers, data=data)
    #now return json data in content from results obj - goal: convert json data(str) into py dictionary to be able to access data
    #loads stands for load str
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token
token = get_token()

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

#Primera función 1.1

def search_for_artist(token, artist_name):
    url="https://api.spotify.com/v1/search"
    headers=get_auth_header(token)
    query= f"?q={artist_name}&type=artist&limit=1"
    query_url= url + query
    result = get(query_url, headers=headers)
    data = json.loads(result.content)['artists']['items']
    if len(data) == 0:
        print('No artist found with this name...')
        return None
    if len(data) > 0:
        for artist in data:
            print(artist['name'])
            print("Artist ID: " + artist['id'] + ' click here to access: ' + artist['external_urls']['spotify'])
            print("------")   
        return data[0]

artists_name = search_for_artist(token, artist_name=search_artist) #search_artist is the input in line 8
artists_name_id =artists_name['id']
print(artists_name_id)
   #función 3: nueva función 1.2
def top_tracks_by_artist(token, artist_id):
    url = "https://api.spotify.com/v1/artists/"
    query= f"{artist_id}/top-tracks?market=ES"
    query_url= url + query
    headers = get_auth_header(token)
    result = get(query_url, headers=headers)
    data = json.loads(result.content)['tracks']
    if len(data) > 0:
        for track in data:
            print(track['name'])
            print("------")
        return data[0]
    else:
        print("We didn't find your track")
    return data
top_tracks_by_artist(token, artist_id=artists_name_id)
   


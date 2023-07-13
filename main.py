import base64
from requests import post, get
import json


client_id = 'cf3cd5f150b14c1da25f369e03a8fbf8'
client_secret = '20ade54cfa7e4666b588ef19a8c41f19'

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

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def song_search(token, song_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={song_name}&type=track&limit=1"

#combine url&query component. Question mark can be incl into query str so it's cleaner
    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    print(json_result)

token = get_token()
song_search(token, "Supermassive Black Hole")


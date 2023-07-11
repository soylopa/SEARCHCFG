import base64
from requests import post, get
import json

client_id = 'c1fb38329c7e43be8ad7d9887649a609'
client_secret = 'c534942543d24b9c86a519209cf6efe3'

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
print(token)

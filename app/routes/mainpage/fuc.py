from dotenv import load_dotenv
import os
import urllib.parse
from app.model.connection import mongodb

client = mongodb.get_client()
db = client['hellody']
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

REDIRECT_URI = 'http://localhost:8000/callback'

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1/'

def login():
    #session = request.session
    #if session.get('access_token'):
    #    return RedirectResponse('/me') 
    scope = 'user-read-currently-playing user-read-recently-played user-read-private user-read-email playlist-read-private playlist-read-collaborative user-read-recently-played'
    auth_url = get_auth_url(scope)
    #auth_url = json.load(auth_url)
    return auth_url

def get_auth_url(scope):
    params = {
        'client_id' : CLIENT_ID,
        'response_type' : 'code',
        'scope' : scope,
        'redirect_uri' : REDIRECT_URI
    } 
    return f"{AUTH_URL}?{urllib.parse.urlencode(params)}"

async def check_Spotify_accesstoken(user_id: int):
    collection = db['USERS']
    status = await collection.find_one({'USER_ID': user_id}, {'SPOTIFY': 1})
    print(status)
    return status['SPOTIFY']

async def vodlist_spotify(user_id: int):
    collection = db['recommend_list']
    cursor = collection.find({'user_id': user_id}, {'_id': 0, 'spotify': 1})
    vod_list = await cursor.to_list(length=100)
    print(vod_list)
    return vod_list

async def vodlist_youtube(user_id: int):
    collection = db['recommend_list']
    cursor = collection.find({'user_id': user_id}, {'_id': 0, 'youtube': 1})
    vod_list = await cursor.to_list(length=100)
    print(vod_list)
    return vod_list

async def vodlist_watch(user_id: int):
    collection = db['recommend_list']
    cursor = collection.find({'user_id': user_id}, {'_id': 0, 'watch': 1})
    vod_list = await cursor.to_list(length=100)
    print(vod_list)
    return vod_list

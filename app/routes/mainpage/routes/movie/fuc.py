
from app.model.connection import mongodb

client = mongodb.get_client()
db = client['hellody']



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

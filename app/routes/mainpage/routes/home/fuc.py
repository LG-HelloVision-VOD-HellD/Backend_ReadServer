
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
    collection = db['youtube_recommend']
    cursor = collection.find({}, {'_id': 0, 'youtube_recommend': 1})
    vod_list = await cursor.to_list(length=100)
    print(vod_list)
    return vod_list

async def vodlist_watch(user_id: int):
    collection = db['recommend_list']
    cursor = collection.find({'user_id': user_id}, {'_id': 0, 'vod_history': 1})
    vod_list = await cursor.to_list(length=100)
    print(vod_list)
    return vod_list

async def vodlist_rating(user_id: int):
    collection = db['recommend_list']
    cursor = collection.find({'user_id': user_id}, {'_id': 0, 'review_rating_based': 1})
    vod_list = await cursor.to_list(length=100)
    print(vod_list)
    return vod_list

async def vodlist_popular(user_id: int):
    collection = db['new_user']
    cursor = collection.find({}, {'_id': 0, 'new_user': 1})
    vod_list = await cursor.to_list(length=100)
    print(vod_list)
    return vod_list[0]['new_user']

async def vodlist_spotify_firstuser(user_id: int):
    try:
        spotify_collection = db['SPOTIFY']
        emotion = await spotify_collection.find_one({'USER_ID':user_id}, {'_id':0, 'EMOTION':1})
        movie_collection = db['MOVIES']
        cursor = movie_collection.find({'EMOTION': emotion['EMOTION']},{'_id':0,'VOD_ID':1, 'TITLE':1, 'POSTER':1})
        vod_list = await cursor.to_list(length=100)
        return vod_list
    except:
        return False
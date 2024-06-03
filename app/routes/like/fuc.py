from app.model.connection import mongodb

client = mongodb.get_client()
db = client['hellody']

vod_types = {"영화" : 'MOVIES', "시리즈" : "SERIES", "키즈" : "KIDS"}
#제목, 배우
async def get_like_list(user_id):
    collection_likes = db['LIKES']
    cursor = collection_likes.find({'USER_ID': user_id}, {'_id': 0})
    like_lists = await cursor.to_list(length=100)
    collection_title = db['VOD']
    for like_list in like_lists:
        print(like_list)
        title = await collection_title.find_one({'VOD_ID':like_list['VOD_ID']}, {'_id' : 0, 'TITLE':1, 'TYPE':1})
        TYPE = vod_types[title['TYPE']]
        collection_vod = db[TYPE]
        poster  = await collection_vod.find_one({'VOD_ID': like_list['VOD_ID']}, {'_id' : 0, 'POSTER':1})

        like_list['TITLE'] = title['TITLE']
        like_list['POSTER'] = poster['POSTER']
        print(like_list)
    return like_lists
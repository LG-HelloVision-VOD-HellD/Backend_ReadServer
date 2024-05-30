from app.model.connection import mongodb

client = mongodb.get_client()
db = client['hellody']

vod_types = {"영화" : 'MOVIES', "시리즈" : "SERIES", "키즈" : "KIDS"}
#제목, 배우
async def get_review_list(user_id):
    collection_reviews = db['REVIEW']
    cursor = collection_reviews.find({'USER_ID': user_id}, {'_id': 0})
    review_lists = await cursor.to_list(length=100)
    collection_title = db['VOD']
    for review_list in review_lists:
        print(review_list)
        title = await collection_title.find_one({'VOD_ID':review_list['VOD_ID']}, {'_id' : 0, 'TITLE':1, 'TYPE':1})
        TYPE = vod_types[title['TYPE']]
        collection_vod = db[TYPE]
        poster  = await collection_vod.find_one({'VOD_ID': review_list['VOD_ID']}, {'_id' : 0, 'POSTER':1})

        review_list['TITLE'] = title['TITLE']
        review_list['POSTER'] = poster['POSTER']
        print(review_list)
    return review_lists


async def get_review_detail(user_id, review_id):
    collection_reviews = db['REVIEW']
    review_list = await collection_reviews.find_one({'USER_ID': user_id, 'REVIEW_ID': review_id}, {'_id': 0})
    collection_title = db['VOD']
  
    print(review_list)
    title = await collection_title.find_one({'VOD_ID':review_list['VOD_ID']}, {'_id' : 0, 'TITLE':1, 'TYPE':1})
    TYPE = vod_types[title['TYPE']]
    collection_vod = db[TYPE]
    poster  = await collection_vod.find_one({'VOD_ID': review_list['VOD_ID']}, {'_id' : 0, 'POSTER':1})
    review_list['TITLE'] = title['TITLE']
    review_list['POSTER'] = poster['POSTER']
    print(review_list)
    return review_list
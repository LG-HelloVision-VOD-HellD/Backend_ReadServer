from app.model.connection import mongodb

client = mongodb.get_client()
db = client['hellody']

async def search_keyword(keyword: str):
    movie_collection = db['MOVIES']
    cursor = movie_collection.find(
        {
            '$or': [
                {"TITLE": {"$regex": keyword, "$options": "i"}},
                {"GENRE": {"$regex": keyword, "$options": "i"}},
                {"CAST": {"$regex": keyword, "$options": "i"}}
            ]
        },
        {'_id':0, 'VOD_ID':1, 'TITLE':1, 'POSTER':1}
    )
    result = await cursor.to_list(length=100)
    return result

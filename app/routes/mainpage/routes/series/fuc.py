from app.model.connection import mongodb

client = mongodb.get_client()
db = client['hellody']


async def get_comedy_list():
    try:
        comedy_collection = db['SERIES']
        cursor = comedy_collection.find(
            {
                '$or': [
                    {"GENRE":'Reality, 코미디'},
                    {"GENRE":'코미디, Reality'},
                    {"GENRE":'Reality'},
                    {"GENRE":'코미디'}
                ]
            },
            {'_id':0, 'VOD_ID':1, 'TITLE':1, 'POSTER':1}
        )
        comedy_list = await cursor.to_list(length=100)
        return comedy_list
    except:
        return False
    
async def get_drama_list():
    try:
        comedy_collection = db['SERIES']
        cursor = comedy_collection.find(
            {
                "GENRE": {"$regex": '드라마', "$options": "i"}
            },
            {'_id':0, 'VOD_ID':1, 'TITLE':1, 'POSTER':1}
        )
        comedy_list = await cursor.to_list(length=100)
        return comedy_list
    except:
        return False
    
async def get_others_list():
    try:
        comedy_collection = db['SERIES']
        cursor = comedy_collection.find(
            {
                '$nor':[
                    {"GENRE": {"$regex": '드라마', "$options": "i"}},
                    {"GENRE": {"$regex": 'Reality', "$options": "i"}},
                    {"GENRE": {"$regex": '코미디', "$options": "i"}},
                ]
            },
            {'_id':0, 'VOD_ID':1, 'TITLE':1, 'POSTER':1}
        )
        comedy_list = await cursor.to_list(length=100)
        return comedy_list
    except:
        return False


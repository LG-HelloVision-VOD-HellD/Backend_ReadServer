from app.model.connection import mongodb

client = mongodb.get_client()
db = client['hellody']


async def get_popular_list():
    try:
        comedy_collection = db['KIDS']
        cursor = comedy_collection.find(
            {
                'SEASON_SUM':{'$gte': 7}
            },
            {'_id':0, 'VOD_ID':1, 'TITLE':1, 'POSTER':1}
        )
        comedy_list = await cursor.to_list(length=100)
        return comedy_list
    except:
        return False
    
async def get_korea_list():
    try:
        comedy_collection = db['KIDS']
        cursor = comedy_collection.find(
            {
                "GENRE": {"$regex": '애니메이션', "$options": "i"}
            },
            {'_id':0, 'VOD_ID':1, 'TITLE':1, 'POSTER':1}
        )
        comedy_list = await cursor.to_list(length=100)
        return comedy_list
    except:
        return False
    
async def get_others_list():
    try:
        comedy_collection = db['KIDS']
        cursor = comedy_collection.find(
            {
                "GENRE": {"$regex": 'Animation', "$options": "i"}
            },
            {'_id':0, 'VOD_ID':1, 'TITLE':1, 'POSTER':1}
        )
        comedy_list = await cursor.to_list(length=100)
        return comedy_list
    except:
        return False


from app.model.connection import mongodb

client = mongodb.get_client()
db = client['hellody']


async def get_popular_list():
    try:
        comedy_collection = db['KIDS']
        cursor = comedy_collection.find({},
            {'_id':0, 'VOD_ID':1, 'TITLE':1, 'POSTER':1}
        ).sort({'POPULARITY':-1,'FIRST_AIR_DATE':-1})
        comedy_list = await cursor.to_list(length=200)
        return comedy_list
    except:
        return False
    
async def get_recent_list():
    try:
        comedy_collection = db['KIDS']
        cursor = comedy_collection.find({},
            {'_id':0, 'VOD_ID':1, 'TITLE':1, 'POSTER':1}
        ).sort({'FIRST_AIR_DATE':-1, 'POPULARITY':-1})
        comedy_list = await cursor.to_list(length=200)
        return comedy_list
    except:
        return False
    


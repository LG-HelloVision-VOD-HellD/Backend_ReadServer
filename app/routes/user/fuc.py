from app.model.connection import mongodb

client = mongodb.get_client()
db = client['hellody']

async def get_userinfo(user_id:int):
    collection = db['USERS']
    user = await collection.find_one({'USER_ID':user_id}, {'_id':0})
    return user
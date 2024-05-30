from app.model.connection import mongodb

client = mongodb.get_client()
db = client['hellody']

async def get_userlist(settop_num:str):
    collection = db['USERS']
    cursor = collection.find({'SETTOP_NUM':settop_num}, {'_id':0, 'USER_ID':1, 'USER_NAME':1})
    user_list = await cursor.to_list(length=100)
    print(user_list)
    return user_list
from app.model.connection import mongodb

client = mongodb.get_client()
db = client['hellody']

async def get_userlist(settop_num:str):
    collection = db['USERS']
    cursor = collection.find({'SETTOP_NUM':settop_num}, {'_id':0, 'USER_ID':1, 'USER_NAME':1})
    user_list = await cursor.to_list(length=100)
    like_collection = db['LIKES']
    for user in user_list:
        like_status = await like_collection.find_one({'USER_ID':user['USER_ID']},{})
        if like_status:
            user['LIKE_STATUS'] = True
        else:
            user['LIKE_STATUS'] = False
    print(user_list)
    return user_list
from app.model.connection import mongodb

client = mongodb.get_client()
db = client['hellody']
vod_types = {"영화" : 'MOVIES', "시리즈" : "SERIES", "키즈" : "KIDS"}
async def vod_detail(vod_id):
    try:
        vod_collection = db['VOD']
        vod_type = await vod_collection.find_one({'VOD_ID': vod_id}, {'_id':0, 'TYPE': 1})
        vod_type = vod_type['TYPE']
        vod_type = vod_types[vod_type]
        print(vod_type)
        collection = db[vod_type]
        detail_vod = await collection.find_one({'VOD_ID':vod_id}, {'_id': 0})
        print(detail_vod)
        return detail_vod
    except:
        return False
    #collection = db['VOD']

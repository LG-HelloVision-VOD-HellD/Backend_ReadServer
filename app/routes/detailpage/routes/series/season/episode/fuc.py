from app.model.connection import mongodb

client = mongodb.get_client()
db = client['hellody']

async def episode_detail(season_id):
    collection = db['EPISODE']
    cursor = collection.find({'SEASON_ID': season_id}, {'_id': 0})
    vod_list = await cursor.to_list(length=100)
    print(vod_list)
    return vod_list
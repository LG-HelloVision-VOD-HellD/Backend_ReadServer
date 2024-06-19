from app.model.connection import mongodb

client = mongodb.get_client()
db = client['hellody']

async def season_detail(series_id):
    collection = db['KIDS_SEASON']
    cursor = collection.find({'K_SERIES_ID': series_id}, {'_id': 0, 'K_SEASON_ID':1, 'SEASON_NUM':1}).sort({'K_SEASON_NUM':1})
    vod_list = await cursor.to_list(length=100)
    for vod in vod_list:
        episode_count = await collection.find_one({'K_SEASON_ID':vod['K_SEASON_ID']}, {'_id':0, 'EPISODE_COUNT':1})
        vod['EPISODE_COUNT'] = episode_count['EPISODE_COUNT']
    print(vod_list)
    return vod_list
    
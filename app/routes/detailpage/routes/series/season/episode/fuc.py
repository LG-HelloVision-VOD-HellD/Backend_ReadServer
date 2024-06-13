from app.model.connection import mongodb

client = mongodb.get_client()
db = client['hellody']
url = 'https://image.tmdb.org/t/p/original'
async def episode_detail(season_id):
    episode_collection = db['EPISODE']
    cursor = episode_collection.find({'SEASON_ID': season_id}, {'_id': 0}).sort({'EPISODE_NUM':1})
    season_collection = db['SEASON']
    series_id = await season_collection.find_one({'SEASON_ID':season_id},{'_id':0, 'SERIES_ID':1})
    print(series_id)
    series_collection = db['SERIES']
    poster = await series_collection.find_one({'SERIES_ID':series_id['SERIES_ID']},{'_id':0, 'POSTER':1})
    vod_list = await cursor.to_list(length=100)
    for vod in vod_list:
        if vod['EPISODE_STILL'] is None:
            vod['EPISODE_STILL'] = poster['POSTER']
        else:
            vod['EPISODE_STILL'] = url+vod['EPISODE_STILL']
    print(vod_list)
    return vod_list

from app.model.connection import mongodb

client = mongodb.get_client()
db = client['hellody']
collection = db['MOVIES']


async def sf_fantasy():
    cursor = collection.find(
        {
            '$or': [
                {'GENRE': {'$regex': '^SF'}},
                {'GENRE': {'$regex': '^판타지'}},
                {'GENRE': {'$regex': '^미스터리'}}
            ]
        },
        {'_id': 0, 'VOD_ID': 1, 'TITLE': 1, 'POSTER': 1}
    )
    vod_list = await cursor.to_list(length=100)
    return vod_list


async def liberal_others():
    cursor = collection.find(
        {
            '$or': [
                {'GENRE': {'$regex': '^TV영화'}},
                {'GENRE': {'$regex': '^다큐멘터리'}},
                {'GENRE': {'$regex': '^서부'}},
                {'GENRE': {'$regex': '^역사'}}
            ]
        },
        {'_id': 0, 'VOD_ID': 1, 'TITLE': 1, 'POSTER': 1}
    )
    vod_list = await cursor.to_list(length=100)
    return vod_list

async def family():
    cursor = collection.find(
        {
            '$or': [
                {'GENRE': {'$regex': '^가족'}},
                {'GENRE': {'$regex': '^코미디'}}
            ]
        },
        {'_id': 0, 'VOD_ID': 1, 'TITLE': 1, 'POSTER': 1}
    )
    vod_list = await cursor.to_list(length=100)
    return vod_list

async def honor():
    cursor = collection.find(
        {
            '$or': [
                {'GENRE': {'$regex': '^공포'}},
                {'GENRE': {'$regex': '^범죄'}},
                {'GENRE': {'$regex': '^스릴러'}}
            ]
        },
        {'_id': 0, 'VOD_ID': 1, 'TITLE': 1, 'POSTER': 1}
    )
    vod_list = await cursor.to_list(length=100)
    return vod_list

async def drama():
    cursor = collection.find(
        {
            '$or': [
                {'GENRE': {'$regex': '^드라마'}},
                {'GENRE': {'$regex': '^음악'}}
            ]
        },
        {'_id': 0, 'VOD_ID': 1, 'TITLE': 1, 'POSTER': 1}
    )
    vod_list = await cursor.to_list(length=100)
    return vod_list

async def romance():
    cursor = collection.find(
        {
            '$or': [
                {'GENRE': {'$regex': '^로맨스'}}
            ]
        },
        {'_id': 0, 'VOD_ID': 1, 'TITLE': 1, 'POSTER': 1}
    )
    vod_list = await cursor.to_list(length=100)
    return vod_list

async def action():
    cursor = collection.find(
        {
            '$or': [
                {'GENRE': {'$regex': '^액션'}},
                {'GENRE': {'$regex': '^모험'}},
                {'GENRE': {'$regex': '^전쟁'}}
            ]
        },
        {'_id': 0, 'VOD_ID': 1, 'TITLE': 1, 'POSTER': 1}
    )
    vod_list = await cursor.to_list(length=100)
    return vod_list

async def animations():
    cursor = collection.find(
        {
            '$or': [
                {'GENRE': {'$regex': '^애니메이션'}}
            ]
        },
        {'_id': 0, 'VOD_ID': 1, 'TITLE': 1, 'POSTER': 1}
    )
    vod_list = await cursor.to_list(length=100)
    return vod_list
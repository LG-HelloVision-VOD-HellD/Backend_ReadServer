
from app.model.connection import mongodb

client = mongodb.get_client()
db = client['hellody']
collection = db['SERIES']


async def action_fantasy():
    cursor = collection.find(
        {
            '$or': [
                {'GENRE': {'$regex': '^Action'}},
                {'GENRE': {'$regex': '^Sci-Fi'}},
                {'GENRE': {'$regex': '^War'}},
                {'GENRE': {'$regex': '^미스터리'}},
                {'GENRE': {'$regex': '^범죄'}}
            ]
        },
        {'_id': 0, 'VOD_ID': 1, 'TITLE': 1, 'POSTER': 1}
    )
    vod_list = await cursor.to_list(length=100)
    return vod_list


async def family_comedy():
    cursor = collection.find(
        {
            '$or': [
                {'GENRE': {'$regex': '^Animation'}},
                {'GENRE': {'$regex': '^Comedy'}},
                {'GENRE': {'$regex': '^Family'}},
                {'GENRE': {'$regex': '^가족'}},
                {'GENRE': {'$regex': '^애니메이션'}},
                {'GENRE': {'$regex': '^코미디'}}
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
                {'GENRE': {'$regex': '^Drama'}},
                {'GENRE': {'$regex': '^드라마'}}
            ]
        },
        {'_id': 0, 'VOD_ID': 1, 'TITLE': 1, 'POSTER': 1}
    )
    vod_list = await cursor.to_list(length=100)
    return vod_list

async def reality():
    cursor = collection.find(
        {
            '$or': [
                {'GENRE': {'$regex': '^Reality'}}
            ]
        },
        {'_id': 0, 'VOD_ID': 1, 'TITLE': 1, 'POSTER': 1}
    )
    vod_list = await cursor.to_list(length=100)
    return vod_list


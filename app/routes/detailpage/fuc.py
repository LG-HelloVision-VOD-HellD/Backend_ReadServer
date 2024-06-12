from app.model.connection import mongodb

client = mongodb.get_client()
db = client['hellody']
vod_types = {"영화" : 'MOVIES', "시리즈" : "SERIES", "키즈" : "KIDS"}
async def vod_detail(vod_id, user_id):
    try:
        vod_collection = db['VOD']
        vod_type = await vod_collection.find_one({'VOD_ID': vod_id}, {'_id':0, 'TYPE': 1})
        vod_type = vod_type['TYPE']
        vod_type = vod_types[vod_type]
        print(vod_type)
        #배우 프로필 추가
        collection = db[vod_type]
        detail_vod = await collection.find_one({'VOD_ID':vod_id}, {'_id': 0})
        if vod_type == 'MOVIES':
            actor_collection = db['ACTOR']
            cursor = actor_collection.find({'MOVIE_ID':detail_vod['MOVIE_ID']}, {'_id':0, 'ACTOR_NAME':1,'PROFILE':1})
            actor = await cursor.to_list(length=100)
            detail_vod['ACTOR'] = actor
        print()
        #리뷰 정보 넣기
        review_collection = db['REVIEW']
        cursor = review_collection.find({'VOD_ID':vod_id}, {'_id':0, 'USER_ID':1, 'RATING':1, 'COMMENT':1, 'M_DATE':1})
        review_lists = await cursor.to_list(length=100)
        for review_list in review_lists:
            user_collection = db['USERS']
            user_name = await user_collection.find_one({'USER_ID':review_list['USER_ID']}, {'_id':0, 'USER_NAME':1})
            review_list["USER_NAME"] = user_name["USER_NAME"]
        detail_vod['review'] = review_lists
        
        #찜 유무 넣기
        like_collection = db['LIKES']
        like_status = await like_collection.find_one({'USER_ID':user_id, 'VOD_ID':vod_id}, {'_id':0})
        if like_status is None:
            like_status = False
        else:
            like_status = True
        detail_vod['like_status'] = like_status
        #해당 관련 VOD 추천 VOD 목록
        genre = detail_vod['GENRE'].split(', ')
        genre = genre[0]
        cursor = collection.find(
            {"GENRE": {"$regex": genre, "$options": "i"}}, {'_id':0, 'VOD_ID':1, 'TITLE':1, 'POSTER':1})
        recommend_vod = await cursor.to_list(length=100)
        detail_vod['recommend_list'] = recommend_vod

        print(detail_vod)
        return detail_vod
    
    except:
        return False
    #collection = db['VOD']

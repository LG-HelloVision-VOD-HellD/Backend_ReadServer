from fastapi import APIRouter, HTTPException

from .fuc import check_Spotify_accesstoken, vodlist_spotify, vodlist_youtube, vodlist_watch, login

router = APIRouter(prefix='/mainpage')

@router.get('/vodlist/spotify/{user_id}')
async def magepage_spotify_list(user_id: int):
    try:
        if await check_Spotify_accesstoken(user_id):
            data = await vodlist_spotify(user_id)
            result = {
                'status': True,
                'response': data[0]['spotify']
            }
            return result
        else: 
            result = {
                'status': False
            }
            return result
    except:
        raise HTTPException(status_code=400, detail='error')

@router.get('/vodlist/youtube/{user_id}')
async def magepage_youtude_list(user_id: int):
    try:
        data = await vodlist_youtube(user_id)
        return data[0]['youtube']
    except: 
        raise HTTPException(status_code=400, detail='error')
    
@router.get('/vodlist/watch/{user_id}')
async def magepage_watch_list(user_id: int):
    try:
        data = await vodlist_watch(user_id)
        return data[0]['watch']
    except: 
        raise HTTPException(status_code=400, detail='error')
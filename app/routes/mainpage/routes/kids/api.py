from fastapi import APIRouter, HTTPException
from .fuc import get_popular_list, get_recent_list

router = APIRouter(prefix='/kids')

@router.get('/popularlist')
async def comedy_list():
    result = await get_popular_list()
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail='error')
    
@router.get('/recentlylist')
async def comedy_list():
    result = await get_recent_list()
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail='error')
    

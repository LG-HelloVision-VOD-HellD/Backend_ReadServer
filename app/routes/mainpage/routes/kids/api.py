from fastapi import APIRouter, HTTPException
from .fuc import get_popular_list, get_korea_list, get_others_list

router = APIRouter(prefix='/kids')

@router.get('/popular')
async def comedy_list():
    result = await get_popular_list()
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail='error')
    
@router.get('/korea')
async def comedy_list():
    result = await get_korea_list()
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail='error')
    
@router.get('/others')
async def comedy_list():
    result = await get_others_list()
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail='error')

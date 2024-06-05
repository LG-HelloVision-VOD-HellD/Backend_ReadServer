from fastapi import APIRouter, HTTPException
from .fuc import get_comedy_list, get_drama_list, get_others_list

router = APIRouter(prefix='/series')

@router.get('/comedy')
async def comedy_list():
    result = await get_comedy_list()
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail='error')
    
@router.get('/drama')
async def comedy_list():
    result = await get_drama_list()
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

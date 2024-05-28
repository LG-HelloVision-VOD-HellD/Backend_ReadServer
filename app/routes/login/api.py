from fastapi import APIRouter, HTTPException
from .fuc import get_userlist

router = APIRouter(prefix='/login')

@router.get('/{settop_num}')
async def user_list(settop_num:str):
    try:
        result = await get_userlist(settop_num)
        return result
    except:
        raise HTTPException(status_code=400, detail='error')
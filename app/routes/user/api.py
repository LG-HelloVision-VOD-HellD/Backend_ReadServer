from fastapi import APIRouter, HTTPException
from .fuc import get_userinfo
router = APIRouter(prefix='/user')

@router.get('/{user_id}')
async def user_info(user_id:int):
    try:
        result = await get_userinfo(user_id)
        return result
    except:
        raise HTTPException(status_code=400, detail='error')
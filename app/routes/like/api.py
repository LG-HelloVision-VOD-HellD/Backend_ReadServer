from fastapi import APIRouter, HTTPException
from .fuc import get_like_list

router = APIRouter(prefix='/like')



@router.get('/{user_id}')
async def like_list(user_id: int):
    result = await get_like_list(user_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail='error')
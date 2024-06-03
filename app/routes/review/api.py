from fastapi import APIRouter, HTTPException
from .fuc import get_review_list, get_review_detail

router = APIRouter(prefix='/review')



@router.get('/{user_id}')
async def review_list(user_id: int):
    result = await get_review_list(user_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail='error')
    
@router.get('/{user_id}/{review_id}')
async def review_detail(user_id: int, review_id: int):
    result = await get_review_detail(user_id, review_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail='error')

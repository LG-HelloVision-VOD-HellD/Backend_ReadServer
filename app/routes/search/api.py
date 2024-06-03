from fastapi import APIRouter, HTTPException
from .fuc import search_keyword
router = APIRouter(prefix='/search')

@router.get('/{keyword}')
async def search_vod(keyword:str):
    result = await search_keyword(keyword)
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail='error')
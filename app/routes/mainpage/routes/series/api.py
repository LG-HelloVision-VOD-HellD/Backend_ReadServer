from fastapi import APIRouter, HTTPException
from .fuc import action_fantasy, family_comedy, drama, reality

router = APIRouter(prefix='/series')

@router.get('/action-fantasy')
async def series_action_fantasy_list():
    result = await action_fantasy()
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail='error')
    
@router.get('/family_comedy')
async def series_family_comedy_list():
    result = await family_comedy()
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail='error')
    
@router.get('/drama')
async def series_drama_list():
    result = await drama()
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail='error')
@router.get('/reality')
async def series_reality_list():
    result = await reality()
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail='error')
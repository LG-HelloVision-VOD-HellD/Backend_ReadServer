from fastapi import APIRouter, HTTPException
from .fuc import episode_detail

router = APIRouter(prefix='/kids_episode_detail')



@router.get('/{season_id}')
async def kids_episode(season_id: int):
    result = await episode_detail(season_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail='error')
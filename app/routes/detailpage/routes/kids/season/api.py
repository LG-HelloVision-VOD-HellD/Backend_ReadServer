from fastapi import APIRouter, HTTPException
from .fuc import season_detail
from .episode.api import router as series_episode_router

router = APIRouter(prefix='/kids_season_detail')

router.include_router(series_episode_router)

@router.get('/{series_id}')
async def kids_season(series_id: int):
    result = await season_detail(series_id)
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=400, detail='error')
    
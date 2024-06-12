from fastapi import APIRouter, HTTPException
from .fuc import vod_detail
from .routes.series.season.api import router as series_router
from .routes.kids.season.api import router as kids_router
router = APIRouter(prefix='/detailpage')

router.include_router(series_router)
router.include_router(kids_router)

@router.get('/vod_detail/{vod_id}/{user_id}')
async def vod_detailpage(vod_id: int, user_id:int):
    result = await vod_detail(vod_id, user_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail='error')


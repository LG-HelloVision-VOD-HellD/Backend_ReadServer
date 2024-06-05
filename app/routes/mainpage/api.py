from fastapi import APIRouter, HTTPException
from .routes.movie.api import router as movie_router
from .routes.series.api import router as series_router
from .routes.kids.api import router as kids_router
router = APIRouter(prefix='/mainpage')

router.include_router(movie_router)
router.include_router(series_router)
router.include_router(kids_router)

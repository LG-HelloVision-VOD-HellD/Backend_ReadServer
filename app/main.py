from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from .routes.mainpage.api import router as mainpage_router
from .routes.detailpage.api import router as detailpage_router
from .routes.user.api import router as user_router
from .routes.login.api import router as login_router
from .routes.like.api import router as like_router
from .routes.review.api import router as review_router
from .routes.search.api import router as search_router
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # 허용할 origin을 설정하세요
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(mainpage_router)
app.include_router(detailpage_router)
app.include_router(user_router)
app.include_router(login_router)
app.include_router(like_router)
app.include_router(review_router)
app.include_router(search_router)
@app.get('/')
async def index():
    return "hellody read-server"

if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port = 80, reload=True)

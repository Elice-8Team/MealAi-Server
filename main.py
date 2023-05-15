from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.database.database import engine
from app.database.token import Redis
from app.error.base import CustomException
from app.model import auth as model_auth
from app.model import feed as model_feed
from app.model import like as model_like
from app.model import user as model_user
from app.router import user, feed, auth, report

model_feed.Base.metadata.create_all(bind=engine)
model_user.Base.metadata.create_all(bind=engine)
model_like.Base.metadata.create_all(bind=engine)
model_auth.Base.metadata.create_all(bind=engine)

app = FastAPI()


origins = [
    "http://localhost:3000",
    "https://meal-ai-client-git-dev-client-meal-ai.vercel.app",
    "https://meal-ai-client.vercel.app",
    "http://kdt-ai6-team08.elicecoding.com",
]

redis = Redis()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(feed.router)
app.include_router(report.router)


@app.exception_handler(CustomException)
async def custom_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status,
        content={
            "error_code": exc.error_code,
            "error_name": exc.error_name,
            "message": exc.message,
        },
    )

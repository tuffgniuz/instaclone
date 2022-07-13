from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from beanie.odm.utils.general import init_beanie

from src.models.post import Post

from .api.v1.posts import router as PostRouter
from .db.db import db

app = FastAPI()

app.include_router(PostRouter)

origins = ['http://192.168.1.3/4000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


@app.on_event('startup')
async def on_startup():
    await init_beanie(
        database=db,
        document_models=[
            Post
        ]
    )

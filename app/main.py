from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from . import models
from .database import engine
from .routers import post, user, auth, vote


#no need for this model since i am now using alembic
# models.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

#this is not necessary but make i leave am
@app.get("/")
async def root():
    return {"message": "wow,my first website !!"}







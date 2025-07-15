from fastapi import FastAPI
from routers import users, posts, comments
from database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(comments.router)
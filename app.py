import logging

from fastapi import FastAPI

from blog.routers import auth_router

logging.basicConfig(
    level=logging.INFO,
)

app = FastAPI()

app.include_router(auth_router)

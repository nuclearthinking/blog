import logging

from fastapi import FastAPI
from starlette.responses import RedirectResponse

from blog.exceptions import NotAuthorizedException
from blog.routers import auth_router, main_router

logging.basicConfig(
    level=logging.INFO,
)

app = FastAPI()

app.include_router(auth_router)
app.include_router(main_router)


@app.exception_handler(NotAuthorizedException)
async def not_authorized_redirect(*_, **__) -> RedirectResponse:
    return RedirectResponse(url="/login")

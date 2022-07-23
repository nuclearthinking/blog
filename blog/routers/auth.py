from fastapi import APIRouter, HTTPException, Response
from starlette.status import HTTP_200_OK

from blog.exceptions import UserAlreadyExists
from blog.repository.user import create_user
from blog.routers.schemes import RegisterRequest

router = APIRouter()


@router.post("/login")
async def login():
    ...


@router.delete("/logout")
async def logout():
    ...


@router.post('/register')
async def register(register_request: RegisterRequest):
    try:
        await create_user(register_request.email, password=register_request.password)
    except UserAlreadyExists:
        raise HTTPException(status_code=400, detail=f'User with email {register_request.email} already exist')
    return Response(status_code=HTTP_200_OK)

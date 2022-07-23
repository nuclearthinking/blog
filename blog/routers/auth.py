from fastapi import APIRouter

router = APIRouter()


@router.post("/login")
async def login():
    ...


@router.delete("/logout")
async def logout():
    ...

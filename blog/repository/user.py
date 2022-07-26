import sqlalchemy as sa

from blog.database import db_session
from blog.exceptions import UserAlreadyExists, UserNotFound
from blog.models.user import User


async def create_user(email: str, password: str) -> None:
    query = sa.select(User).where(User.email == email)
    result = await db_session.execute(query)
    user = result.scalar_one_or_none()
    if user:
        raise UserAlreadyExists(f"User wit email {email} already exist")
    user = User(
        email=email,
    )
    user.password = password
    db_session.add(user)
    await db_session.commit()


async def get_user(email: str) -> User:
    query = sa.select(User).where(User.email == email)
    result = await db_session.execute(query)
    if user := result.scalar_one_or_none():
        return user
    else:
        raise UserNotFound(f"User with email {email} not found")

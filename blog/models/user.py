import sqlalchemy as sa
from passlib.context import CryptContext

from blog.models.base import BaseDatabaseModel

pwd_context = CryptContext(
    schemes=["pbkdf2_sha512"],
    deprecated="auto",
)


class PasswordHash:
    def __init__(self, _hash: str) -> None:
        self._hash = _hash

    def __eq__(self, o: str) -> bool:
        return pwd_context.verify(o, self._hash)


class User(BaseDatabaseModel):
    __tablename__ = "user"

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    email: str = sa.Column(sa.Text, unique=True, nullable=False)
    _password: str = sa.Column(sa.Text, nullable=False, name="password")

    @property
    def password(self):
        return PasswordHash(self._password)

    @password.setter
    def password(self, value):
        self._password = pwd_context.hash(value)

from pydantic import BaseSettings


class Settings(BaseSettings):
    database_uri: str = "sqlite:///data.db"


settings = Settings()

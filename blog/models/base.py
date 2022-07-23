from blog.database import Base


class BaseDatabaseModel(Base):
    __abstract__ = True

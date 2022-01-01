from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from config import db_uri
# Tutorial = https://stribny.name/blog/fastapi-asyncalchemy/
# Alembic = https://ahmed-nafies.medium.com/tutorial-fastapi-sqlalchemy-postgresql-alembic-and-docker-part-2-asynchronous-version-8a339ce97e6d


if db_uri.connection_type == 'async':
    print('creating async connection')
    engine = create_async_engine(db_uri.database_uri, echo=False)
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )

else:
    print('creating sync connection')
    engine = create_engine(db_uri.database_uri)
    session = sessionmaker(bind=engine)


@as_declarative()
class Base:
    id: Any
    __name__: str


    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


# good example

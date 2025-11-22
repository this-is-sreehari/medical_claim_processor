from sqlalchemy.orm import declarative_base
from typing import AsyncGenerator
from sqlalchemy import DateTime
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession,async_sessionmaker
import datetime
from .config import SQLALCHEMY_DB_URL

Base = declarative_base(
    type_annotation_map = {
        datetime.datetime: DateTime(timezone=True)
    }
)

engine = create_async_engine(
    SQLALCHEMY_DB_URL,
    echo=True
)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as db_session:
        yield db_session

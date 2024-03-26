from sqlalchemy.orm import sessionmaker
from sqlmodel import  SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

from settings import *



DATABASE_URI = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@db:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(DATABASE_URI, echo=True)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
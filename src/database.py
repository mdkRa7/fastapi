from sqlalchemy import String, select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import Annotated, Optional



import os
from pathlib import Path

# 1. Вычисляем путь к папке, где лежит САМ этот файл (database.py)
# То есть путь до папки src/
BASE_DIR = Path(__file__).resolve().parent

# 2. Соединяем путь папки с именем файла базы
DB_PATH = BASE_DIR / "movies_test.db"
print(DB_PATH)
# 3. Подставляем в движок
# На Windows для SQLite нужно 3 слэша + полный путь
async_engine = create_async_engine(f"sqlite+aiosqlite:///{DB_PATH}")

async_session = async_sessionmaker(async_engine, expire_on_commit=False)


async def get_session():
    async with async_session() as session:
        yield session




intpk = Annotated[int, mapped_column(primary_key=True)]


str_500 = Annotated[int, 500]
class Base(DeclarativeBase):
    type_annotation_map = {
        str_500: String(500)
    }
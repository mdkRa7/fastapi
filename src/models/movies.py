from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import Annotated, Optional

from src.database import Base, intpk, str_500


class MoviesModel(Base):
    __tablename__ = "movies"
    id: Mapped[intpk]
    title: Mapped[str_500]
    producer: Mapped[str]
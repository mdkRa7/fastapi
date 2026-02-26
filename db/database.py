import asyncio

from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import Annotated, Optional
from sqlalchemy import String, select



app = FastAPI()
async_engine = create_async_engine('sqlite+aiosqlite:///db/movies.db')

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


class MoviesModel(Base):
    __tablename__ = "movies"
    id: Mapped[intpk]
    title: Mapped[str_500]
    producer: Mapped[str]

@app.post("/setup_database")
async def create_movies():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.run_sync(Base.metadata.create_all)

    return {"message": "success"}

class MovieAddSchema(BaseModel):
    title: str = Field(max_length=500)
    producer: str

class MovieSchema(MovieAddSchema):
    id: int

async def get_session():
    async with async_session() as session:
        yield session




SessionDep = Annotated[AsyncSession, Depends(get_session)]

@app.post("/insert_post")
async def add_movies(new_movie: MovieAddSchema, session: SessionDep):
        new_movie = MoviesModel(title=new_movie.title, producer=new_movie.producer)
        session.add(new_movie)
        await session.commit()
        return {"success":"True"}


@app.get("/movies")
async def get_all_movies(session: SessionDep):
        query = (
            select(MoviesModel)
        )
        result = await session.execute(query)
        return result.scalars().all()
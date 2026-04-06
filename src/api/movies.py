
from fastapi import APIRouter
from src.api.dependencies import PaginationDep
from src.api.dependencies import SessionDep
from src.database import async_engine, Base
from src.models.movies import MoviesModel
from src.schemas.movies import MovieAddSchema, MovieSchema
from sqlalchemy import select

movies_router = APIRouter()


@movies_router.post("/setup_database")
async def create_movies():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.run_sync(Base.metadata.create_all)

    return {"message": "success"}

@movies_router.post("/insert_post")
async def add_movies(new_movie: MovieAddSchema, session: SessionDep):
        new_movie = MoviesModel(title=new_movie.title, producer=new_movie.producer)
        session.add(new_movie)
        await session.commit()

        return {"success":"True"}

#
# @movies_router.get("/movies", response_model=list[MovieSchema])
# async def get_all_movies(session: SessionDep):
#         query = (
#             select(MoviesModel)
#         )
#         result = await session.execute(query)
#         return result.scalars().all()

@movies_router.get("/movies", response_model=list[MovieSchema])
async def get_all_movies(session: SessionDep, pagination: PaginationDep) -> list[MovieSchema]:
    query = (
        select(MoviesModel)
        .limit(pagination.limit)
        .offset(pagination.offset)
    )
    result = await session.execute(query)
    return result.scalars().all()

import asyncio

import uvicorn
from fastapi import FastAPI, HTTPException, Response, Request
from pydantic import BaseModel
import time
from typing import Callable

app = FastAPI()

movies = [
    {
        "id": 1,
        "title": "Бешеные псы",
        "rate": 5
    },
    {
        "id":2,
        "title": "Кримианльное чтиво",
        "rate": 4
    }
]

@app.middleware("http")
async def my_middleware(request: Request, call_next: Callable):
    ip_addres = request.client.host
    print(f"{ip_addres=}")
    # if ip_addres in ['127.0.0.1']:
    #     return Response(content="Ошибка", status_code=492)

    start = time.perf_counter()
    response = await call_next(request)
    print(f'-----------------------{time.perf_counter() - start}-----------------------------')
    response.headers["Chlen"] = "Dildo"
    return response



@app.get("/movies",
         tags=["Фильмы🎥"],
         summary="Get all movies")
async def get_movies():
    await asyncio.sleep(0.5)
    print("хуй")
    return movies

#
# @app.get("/movies{arg}",
#          tags=["Фильмы🎥"],
#          summary="Get a movie")
# def get_movie(arg: int):
#     for mov in movies:
#         if mov["id"] == arg:
#             return mov
#     raise HTTPException(status_code=404, detail="Фильма нет")
#
#
# class NewMovie(BaseModel):
#     title: str
#     rate: int
#
# @app.post("/movies",
#         tags = ["Фильмы🎥"],
#         summary = "Create a movie"
# )
# def create_movie(new_movie: NewMovie):
#     movies.append({
#             "id": len(movies)+1,
#             "title": new_movie.title,
#             "rate": new_movie.rate
#     })
#     return {"message: success"}


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)

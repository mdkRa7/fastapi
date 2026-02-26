import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

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

@app.get("/movies",
         tags=["Фильмы🎥"],
         summary="Get all movies")
def get_movies():
    return movies


@app.get("/movies{arg}",
         tags=["Фильмы🎥"],
         summary="Get a movie")
def get_movie(arg: int):
    for mov in movies:
        if mov["id"] == arg:
            return mov
    raise HTTPException(status_code=404, detail="Фильма нет")


class NewMovie(BaseModel):
    title: str
    rate: int

@app.post("/movies",
        tags = ["Фильмы🎥"],
        summary = "Create a movie"
)
def create_movie(new_movie: NewMovie):
    movies.append({
            "id": len(movies)+1,
            "title": new_movie.title,
            "rate": new_movie.rate
    })
    return {"message: success"}


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)

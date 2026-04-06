import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, Field

app = FastAPI()

data = [
    {
        "id": 1,
        "car_model": "Mazda",
        "year": 2002,
        "country": "Japan",
    },
    {
        "id": 2,
        "car_model": "BMV",
        "year": 2016,
        "country": "Germany",
    }
]


@app.get("/cars", tags=["cars🚚"], summary="получить тачки",
         description="<h1>Отдает список всех книг<h1>")
async def get_cars():
    return data


@app.get("/cars/{car_name}",
         tags=["cars🚚"],)
async def get_car(car_name: str):
    match = next((car for car in data if car["car_model"].lower() == car_name.lower()), None)
    if match is None:
        raise HTTPException(status_code=404, detail="Машина не найдена")
    return match

class CarAddSchema(BaseModel):
    car_model: str = Field(max_length=30)
    year: int = Field(ge=1900, lt=2026)
    country: str = Field(max_length=50)

    model_config = ConfigDict(extra="forbid")


@app.put("/car/{car_id}",
          tags=["cars🚚"])
async def update_car(car_id: int, new_data: CarAddSchema):
    match = next((car for car in data if car["id"] == car_id), None)
    if match is None:
        raise HTTPException(status_code=404, detail=f"Машина не найдена с id: {car_id}")
    match |= new_data.model_dump()
    return {"success": "True"}

# class CarSchema(CarAddSchema):
#     id: int

@app.post("/cars", tags=["cars🚚"], summary="добавить тачку", )
async def add_cars(new_car: CarAddSchema):
    next_number = len(data) + 1
    data.append({"id": next_number,
                 "car_model": new_car.car_model,
                 "year": new_car.year,
                 "country": new_car.country})

    return {"success": "True"}

@app.delete("/car/{car_id}",
            tags=["cars🚚"])
async def delete_car(car_id: int):
    match = next((car for car in data if car["id"] == car_id), None)
    if match is None:
        raise HTTPException(status_code=404,
                            detail="Машина не найдена")
    data.remove(match)
    return {"success": "True"}

if __name__ == '__main__':
    uvicorn.run("test1:app", reload=True, host="0.0.0.0")

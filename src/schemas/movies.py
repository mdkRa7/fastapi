

from pydantic import BaseModel, Field


class MovieAddSchema(BaseModel):
    title: str = Field(max_length=500)
    producer: str

class MovieSchema(MovieAddSchema):
    id: int

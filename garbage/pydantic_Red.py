from pydantic import BaseModel, Field, EmailStr, ConfigDict
from fastapi import FastAPI

app = FastAPI()

data = {
    "email": "fdfd@gmail.ru",
    "title": "SJFDHGDFDd",
    "age": 2
}

data2 = {
    "email": "fdfd@gmail.ru",
    "title": "SJFDHGDFDd",
    # "gender": "male",
    # "birthday": "3432"
}


class UserSchema(BaseModel):
    email: EmailStr
    title: str | None = Field(max_length=10)

    model_config = ConfigDict(extra="forbid")

users = []

@app.post("/users",
          tags=["General"],
          summary="Introduce yourself!",
        )
def create_user(new_user: UserSchema):
    users.append(new_user)
    return {"success": True, "msg": "Everything is good"}

@app.get("/users", tags=["General"], summary="Introduce yourself!",)
def create_user() -> list[UserSchema]:
    return users

class UserAddAgeSchema(UserSchema):
    age: int = Field(ge=0, le=100)

print(repr(UserAddAgeSchema(**data)))
print(repr(UserSchema(**data2)))

# print(UserSchema(**data).__annotations__)
# print(UserSchema(**data).model_fields)
# print(UserSchema(**data).__dict__)
# print(UserSchema.__dict__)




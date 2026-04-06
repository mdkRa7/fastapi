from fastapi import FastAPI, HTTPException, Response, Depends
from authx import AuthXConfig, AuthX
from pydantic import BaseModel

config = AuthXConfig()
config.JWT_SECRET_KEY = "SECRET KEY"
config.JWT_ACCESS_COOKIE_NAME = "my_jwt_cooki"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)

app = FastAPI()


class UserLoginSchema(BaseModel):
    login: str
    password: int


@app.post("/login")
def login(credentials: UserLoginSchema, response: Response):
    if credentials.login == "tests" and credentials.password == 123:
        token = security.create_access_token(uid="12345")
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return {"access_token": token}
    raise HTTPException(detail="Error", status_code=401)


@app.get("/protected", dependencies=[Depends(security.access_token_required)])
def protected():
    return {"data": "Data"}

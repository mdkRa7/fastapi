

from fastapi import FastAPI, Depends
from .api import main_router

app = FastAPI()
app.include_router(main_router)

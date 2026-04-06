from fastapi import APIRouter
from .movies import movies_router


main_router = APIRouter()
main_router.include_router(movies_router)
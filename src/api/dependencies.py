from typing import Annotated

from fastapi import Depends
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_session

SessionDep = Annotated[AsyncSession, Depends(get_session)]


class PaginationParams(BaseModel):
    limit: int = Field(5, description="Max: 100", ge=1, le=100)
    offset: int = Field(0, description="Смещение пагинации", ge=0)


PaginationDep = Annotated[PaginationParams, Depends(PaginationParams)]

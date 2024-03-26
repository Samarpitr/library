from sqlmodel import Field, SQLModel
from typing import Optional


class BookBase(SQLModel):
    title: str = Field(index=True, unique=True)
    author: str
    publication_year: Optional[int] = None

    

class Book(BookBase, table=True):
    id: int = Field(default=None, primary_key=True)


class BookCreate(BookBase):
    pass

class BookUpdate(SQLModel):
    title: Optional[str] = None
    author: Optional[str] = None
    publication_year: Optional[int] = None


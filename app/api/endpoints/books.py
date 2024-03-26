from fastapi import APIRouter, Depends, HTTPException

from sqlmodel.ext.asyncio.session import AsyncSession
from app.db.db_setup import get_session
from sqlmodel import select


from app.models.books import Book, BookCreate, BookUpdate


books_router = APIRouter(tags=["books"])


@books_router.get("/books", response_model=list[Book])
async def get_songs(session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(Book))
    books = result.fetchall()
    return books



@books_router.get("/books/{id}", response_model=Book)
async def get_songs(id: int, session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(Book).filter_by(id=id))
    book = result.first()
    if not book :
        raise HTTPException(status_code=404, detail="Book not found")
    return book



async def check_book_exists_by_title(title: str, session: AsyncSession):
    result = await session.exec(select(Book).filter_by(title=title))
    existing_book = result.all()
    if existing_book:
        return True
    return False

@books_router.post("/books", response_model=Book)
async def create_book(book_data: BookCreate, session: AsyncSession = Depends(get_session)):
    book = Book.model_validate(book_data)
    if await check_book_exists_by_title(book.title, session):
        raise HTTPException(status_code=406, detail="Book with the same title already exists.")
    session.add(book)
    await session.commit()
    return book



@books_router.put("/books/{id}", response_model=Book)
async def update_book(id: int, book_data: BookUpdate, session: AsyncSession = Depends(get_session)):
    book = Book.model_validate(book_data)
    result = await session.get(Book, id)
    if not result:
        raise HTTPException(status_code=404, detail="Book not found")
    data = book_data.model_dump(exclude_unset=True)
    result.sqlmodel_update(data)
    session.add(result)
    await session.commit()
    return result


@books_router.delete("/books/{id}")
async def delete_book(id: int, session: AsyncSession = Depends(get_session)):
    book = await session.get(Book, id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    await session.delete(book)
    await session.commit()
    return {"result" : "Book has been deleted."}

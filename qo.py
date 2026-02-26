# from fastapi import FastAPI, HTTPException
# import uvicorn
# from pydantic import BaseModel
#
# app = FastAPI()
#
# books = [
#     {
#         "id": 1,
#         'title': "Ассинхронность в Python",
#         'author': "Я"
#     },
#     {
#         "id": 2,
#         'title': "вава",
#         'author': "аава"
#     }
#
# ]
#
# @app.get("/books", summary="Книги", tags=["Книги"])
# def read_books():
#     return books
#
# @app.get("/books/{book_id}", summary="Книга", tags=["Книги"])
# def get_book(book_id: int):
#     for book in books:
#         if book["id"] == book_id:
#             return book
#     raise HTTPException(status_code=404, detail="Книга не найдена")
#
# class NewBook(BaseModel):
#     title: str
#     author: str
#
# @app.post("/books", tags=["Книги"])
# def enter_book(new_book: NewBook):
#     books.append({
#         "id": len(books) + 1,
#         "title": new_book.title,
#         'author': new_book.author,
#     })
#     return {"success": True, "message": 'Книга добавлена'}
# if __name__ == '__main__':
#     uvicorn.run("main:app", reload=True)


from pydantic import BaseModel, Field, EmailStr, ConfigDict

from fastapi import FastAPI

app = FastAPI()

data = {
    "email" : "logo@fj.com",
    "bio" : "fdfdfdfd",
    "age" : 100,

}

data_age = {
    "email": "logo@fj.com",
    "bio": "fdfdfdfd",
    "gender":"mail",
    "birthday": "2022"
}

class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=10)

    model_config = ConfigDict(extra="forbid")

class UserAgeSchema(UserSchema):
    age: int = Field(ge=0, le=100)




print(repr(UserSchema(**data_age)))
print(repr(UserAgeSchema(**data)))
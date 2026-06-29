from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="REST Demo")

# מאגר בזיכרון שמדמה DB
books: dict[int, dict] = {
    1: {"id": 1, "title": "Clean Code", "author": "Robert Martin"},
    2: {"id": 2, "title": "The Pragmatic Programmer", "author": "Hunt & Thomas"},
}


class BookIn(BaseModel):
    title: str
    author: str


@app.get("/books")  # קריאת כל הספרים
def list_books():
    return list(books.values())


@app.get("/books/{book_id}")  # קריאת ספר בודד
def get_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    return books[book_id]


@app.post("/books", status_code=201)  # יצירת ספר
def create_book(book: BookIn):
    new_id = max(books) + 1 if books else 1
    books[new_id] = {"id": new_id, **book.model_dump()}
    return books[new_id]


@app.put("/books/{book_id}")  # עדכון ספר
def update_book(book_id: int, book: BookIn):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    books[book_id] = {"id": book_id, **book.model_dump()}
    return books[book_id]


@app.delete("/books/{book_id}", status_code=204)  # מחיקת ספר
def delete_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    del books[book_id]

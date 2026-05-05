from fastapi import FastAPI
from typing import Dict

app = FastAPI()


books: Dict[int, dict] = {
    1: {"title": "Python Basics", "available": True},
    2: {"title": "AI Fundamentals", "available": True}
}

borrowed = {}


@app.get("/books")
def get_books():
    return books


@app.post("/borrow/{user_id}/{book_id}")
async def borrow_book(user_id: int, book_id: int):
    if book_id not in books:
        return {"status": "error", "message": "Book not found"}

    if not books[book_id]["available"]:
        return {"status": "error", "message": "Book already borrowed"}

    books[book_id]["available"] = False
    borrowed[book_id] = user_id

    return {
        "status": "success",
        "message": "Book returned"
    }

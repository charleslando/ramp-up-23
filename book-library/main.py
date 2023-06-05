from fastapi import FastAPI

app = FastAPI()

# Temporary in-memory storage for books
books = []

@app.post("/books/")
def create_book(title: str, author: str, year: int):
    book = {
        "id": len(books) + 1,
        "title": title,
        "author": author,
        "year": year
    }
    books.append(book)
    return book

@app.get("/books/")
def get_all_books():
    return books

@app.get("/books/{id}")
def get_book_by_id(id: int):
    for book in books:
        if book["id"] == id:
            return book
    return {"error": "Book not found"}

@app.put("/books/{id}")
def update_book(id: int, title: str, author: str, year: int):
    for book in books:
        if book["id"] == id:
            book["title"] = title
            book["author"] = author
            book["year"] = year
            return book
    return {"error": "Book not found"}

@app.delete("/books/{id}")
def delete_book(id: int):
    for index, book in enumerate(books):
        if book["id"] == id:
            return books.pop(index)
    return {"error": "Book not found"}

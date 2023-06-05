from fastapi import FastAPI
from schemas import Book 
import random

app = FastAPI()
# counter = 1
library = {}
@app.post("/books/")
async def add_book(b: Book):

    ident = random.randint(100,999)
    library[ident] = b
    # counter += 1
    return ident

@app.get('/books/')
async def get_all_books():
    return list(library.values())



@app.get("/books/{id}")
async def get_specific_book(id: int):
    return library.get(id, "No book found with that ID")

@app.put("/books/{id}")
async def update_book(id: int, title: str = None, author: str = None, year: int = None):
    keys = library.keys()
    #for book in keys:
    if id in keys:
        book = library.get(id)
        if title:
            book.title = title
        if author:
            book.author = author
        if year:
            book.year = year
        return book
    return {"Book to update not found"}


@app.delete("/books/{id}")
async def delete_book(id: int):
    library.pop(id, "Book to delete was not found")

        
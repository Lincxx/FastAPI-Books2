from fastapi import Body, FastAPI

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description 
        self.rating = rating

BOOKS = [
    Book(1,'Computer Science', 'John Doe', 'A book about computer science', 5),
    Book(2,'Mathematics', 'Jane Doe', 'A book about mathematics', 4),
    Book(3,'Physics', 'John Doe', 'A book about physics', 3),
    Book(4,'Chemistry', 'Jane Doe', 'A book about chemistry', 2),
    Book(5,'Biology', 'John Doe', 'A book about biology', 3)
]


@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post("/create-book")
async def create_book(book_request=Body()):
    BOOKS.append(book_request)
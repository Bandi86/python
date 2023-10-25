from fastapi import FastAPI, Depends

# Custom imports
from auth.auth_handler import oauth2_schema, extract_email_from_token, create_acces_token, is_token_valid

app = FastAPI()

# USER

@app.get("/users", tags=["user"])
def get_all_users(token: str = Depends(oauth2_schema)):
    pass

@app.post("/register", tags=["user"])
def register_user():
    pass

@app.post("/login", tags=["user"])
def login_user():
    pass

@app.put("/user/change_email", tags=["user"])
def update_email(token: str = Depends(oauth2_schema)):
    pass

@app.put("/user/change_pwd", tags=["user"])
def update_password(token: str = Depends(oauth2_schema)):
    pass

@app.delete("/users", tags=["user"])
def delete_current_user():
    pass

# BOOK

@app.get("/books", tags=["book"])
def get_all_book():
    pass

@app.get("/get_book_by_isbn", tags=["book"])
def get_book_by_isbn(isbn: str):
    return {"book": isbn}

@app.get("/get_books_from_author", tags=["book"])
def get_books_from_author(author: str):
    return {"book author" : author}

@app.post("/book/add_single", tags=["book"])
def add_new_book(title: str, author: str, isbn: str, token: str = Depends(oauth2_schema)):
    return {"title" : title, "author" : author, "isbn" : isbn }

@app.post("/book", tags=["book"])
def add_new_books(title: str, author: str, isbn: str, token: str = Depends(oauth2_schema)):
    return {"title" : title, "author" : author, "isbn" : isbn }

@app.delete("/book", tags=["book"])
def delete_book_by_isbn(isbn: str, token: str = Depends(oauth2_schema)):
    pass

@app.put("/book_title", tags=["book"])
def update_book_title(new_title: str, isbn: str, token: str = Depends(oauth2_schema)):
    pass

# BOOKING

@app.get("/booking/all", tags=["booking"])
def get_all_bookings(token: str = Depends(oauth2_schema)):
    pass

@app.get("/booking/user", tags=["booking"])
def get_all_bookings_of_current_user(token: str = Depends(oauth2_schema)):
    pass

@app.get("/booking/book_bookings", tags=["booking"])
def get_all_bookings_of_a_book_by_isbn(isbn: str, token: str = Depends(oauth2_schema)):
    pass

@app.post("/booking/add", tags=["booking"])
def add_single_booking(token: str = Depends(oauth2_schema)):
    pass


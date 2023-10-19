from fastapi import FastAPI, status, HTTPException, Response, Depends
from fastapi.params import Body
from typing import Optional
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
import models
from db import engine, Base, get_db
from sqlalchemy.orm import Session 

#tablak letrehozasa
Base.metadata.create_all(bind=engine)

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # optional field with true
    rating: Optional[int] = None


while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi',
                                user='postgres', password='postgres', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Database connection was succesfull')
        break
    except Exception as error:
        print('Connencting to database failed')
        print('Error: ', error)
        time.sleep(2)

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "favorite foods", "content": "I like pizza", "id": 2}]

# post search by id


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

# removing post

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


@app.get("/")
# a függvény neve nem számít
def read_root():
    return {"Hello": "Wellcome to my API"}

@app.get('/sqlalchemy')
def test_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {'data' : posts }


@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
   # cursor.execute(""" SELECT * FROM posts """)
   # posts = cursor.fetchall()
    posts = db.query(models.Post).all()   
    return {"data": posts}

# title str, content str

# create posts


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    new_post = cursor.execute("""INSERT INTO posts (title, content published) VALUES (%s %s %s) RETURNING * """,
                              (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}

# single post witih id


@app.get("/posts/{id}")
def get_posts(id: int, response: Response):
    cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (str(id),))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No post found with this id: {id}")
    return {"post_detail": post}


# delete post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute(
        """ DELETE FROM posts WHERE id = %s RETURNING * """, (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"no post with this id: {id}")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# update post
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute(""" UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """,
                   (post.title, post.content, post.published, str(id,)))
    updated_post = cursor.fetchone()
    conn.commit()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"no post with this id: {id}")

    return {'data': updated_post}


# dummy route
# hibára fog futni mert először a másik route-ba fog belépni először az id fölé kell tenni


@app.get("/posts/latest")
def get_latest():
    post = my_posts[len(my_posts) - 1]
    return {"detail": post}

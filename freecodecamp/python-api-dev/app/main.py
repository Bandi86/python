from fastapi import FastAPI, status, HTTPException, Response, Depends
from fastapi.params import Body
from typing import Optional
from fastapi.responses import JSONResponse
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from models import Post
from schemas import PostBase, PostCreate, Post
from db import engine, Base, get_db
from sqlalchemy.orm import Session

#tablak letrehozasa
Base.metadata.create_all(bind=engine)

app = FastAPI()


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


@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
   # cursor.execute(""" SELECT * FROM posts """)
   # posts = cursor.fetchall()
    posts = db.query(Post).all()   
    return posts


# CREATE POST

@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model = Post)
def create_posts(post: PostCreate, db: Session = Depends(get_db)):
   # new_post = cursor.execute("""INSERT INTO posts (title, content published) VALUES (%s %s %s) RETURNING * """,
   #                           (post.title, post.content, post.published))
   # new_post = cursor.fetchone()
   # conn.commit()
   
    new_post = Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# SINGLE POST

@app.get("/posts/{id}")
def get_posts(id: int, db: Session = Depends(get_db)):
    #cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (str(id),))
    #post = cursor.fetchone()
    post = db.query(Post).filter(Post.id == id).first()
    if post == None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"no post with this id: {id}")
    return post


# DELETE POST

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    #cursor.execute(
    #    """ DELETE FROM posts WHERE id = %s RETURNING * """, (str(id),))
    #deleted_post = cursor.fetchone()
    #conn.commit()

    post = db.query(Post).filter(Post.id == id)
    
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"no post with this id: {id}")
    
    post.delete(synchronize_session=False)
    db.commit()
    return JSONResponse(content={"message": "Post deleted successfully"})


# UPDATE POST

@app.put("/posts/{id}")
def update_post(id: int, updated_post: PostCreate, db: Session = Depends(get_db)):
    #cursor.execute(""" UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """,
    #               (post.title, post.content, post.published, str(id,)))
    #updated_post = cursor.fetchone()
    #conn.commit()
    post_query = db.query(Post).filter(Post.id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                        detail = f"no post with this id: { id }")
        
    
    post_query.update(updated_post.model_dump(), synchronize_session=False)
    db.commit()
    
    return post_query.first()


# dummy route
# hibára fog futni mert először a másik route-ba fog belépni először az id fölé kell tenni


@app.get("/posts/latest")
def get_latest():
    post = my_posts[len(my_posts) - 1]
    return {"detail": post}

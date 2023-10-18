from fastapi import FastAPI, status, HTTPException, Response
from fastapi.params import Body
from typing import Optional
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # optional field with true
    rating: Optional[int] = None

while True:
    try:
        conn = psycopg2.connect(host= 'localhost', database = 'fastapi', user = 'postgres', password = 'postgres', cursor_factory=RealDictCursor)
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
def get_posts():
    cursor.execute(""" SELECT * FROM posts """)
    posts = cursor.fetchall
    print(posts)
    return {"data": my_posts}

# title str, content str

# create posts

@app.post("/posts", status_code=status.HTTP_201_CREATED) # integrating 201 status code
def create_posts(post: Post):
    posts_dict = post.model_dump()
    # posts_dict['id'] = len(my_posts) + 1
    posts_dict['id'] = randrange(0, 100)
    my_posts.append(posts_dict)
    return {"data": my_posts}

# single post witih id


@app.get("/posts/{id}")
def get_posts(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No post found with this id: {id}")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message" : f"No post found with this id: {id}"}
    return {"post_detail": post}


# delete post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    # find index in the array that has required ID
    # my_posts.pop(index)
    index = find_index_post(id)
    if index == None:
        raise Exception(status_code=status.HTTP_404_NOT_FOUND, detail=f"no post with this id: {id}")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# update post
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise Exception(status_code=status.HTTP_404_NOT_FOUND, detail=f"no post with this id: {id}")
    
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict   
    return {'data': post_dict}


# dummy route
# hibára fog futni mert először a másik route-ba fog belépni először az id fölé kell tenni


@app.get("/posts/latest")
def get_latest():
    post = my_posts[len(my_posts) - 1]
    return {"detail": post}

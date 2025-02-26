import time
from fastapi import FastAPI
from routes import user
from db.connection import engine, Base
import psycopg2
from psycopg2.extras import RealDictCursor
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/api/users")


# Database connection setup
def create_db_connection():
    while True:
        try:
            conn = psycopg2.connect(
                host='localhost',
                database='cube',
                user='postgres',
                password='hardwell86',
                cursor_factory=RealDictCursor
            )
            cursor = conn.cursor()
            print('Database connection was successful')
            return conn, cursor
        except Exception as error:
            print('Connecting to the database failed')
            print('Error:', error)
            time.sleep(5)


# Create database tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"Hello": "Welcome to my API"}

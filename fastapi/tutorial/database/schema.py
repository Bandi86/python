from pydantic import BaseModel, Field, EmailStr
from typing import Union
from typing import List
import datetime

class UserBaseSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

class UserLoginSchema(UserBaseSchema):
    class Config:
        schema_extra = {
            "user" : {
                "email" : "test@test.com",
                "password" : "admin"
            }
        }
 

class UserRegisterSchema(UserBaseSchema):
    fullname: str = Field(default=None)
    class Config:
        schema_extra = {
            "user" : {
                "fullname" : "Suslecz Andras",
                "email" : "test@test.com",
                "password" : "admin"
            }
        }

# Bookings

class BookingBaseSchema(BaseModel):
    from_date : datetime.date = Field(default=None)
    to_date : datetime.date = Field(default=None)
    isbn : str = Field(default=None)
    description : str = Field(default=None)

# Book

class BookBaseSchema (BaseModel):
    isbn: str = Field(default=None)
    title: str = Field(default=None)
    author: str = Field(default=None)

class BookBaseListSchema(BaseModel):
    books: List[BookBaseSchema] = []
    class Config:
        schema_extra = {
            "example" : {
                "books" : [   
                {
                    "title" : "example Title",
                    "isbn" : "asdasd",
                    "author" : "Author1"
                },
                {
                    "title" : "example Title",
                    "isbn" : "asdasd",
                    "author" : "Author1"
                },
                {
                    "title" : "example Title",
                    "isbn" : "asdasd",
                    "author" : "Author1"
                },
                ]
            }
        }
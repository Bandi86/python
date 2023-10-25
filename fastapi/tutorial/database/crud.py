from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy import or_, and_
## User specific imports
from .models import User, Book, Booking
#from .utils import create_timestamp
from .schema import UserRegisterSchema, BookBaseSchema, BookingBaseSchema
#from ..auth.password_handler import verify_password, get_password_hash
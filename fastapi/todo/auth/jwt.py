import time
from datetime import datetime
from database.connection import Settings
from fastapi import HTTPException, status
from jose import JWTError, jwt

settings = Settings()

def create_token(user: str):
    payload = {
        "exp": datetime.utcnow() + settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        "iat": datetime.utcnow(),
        "sub": settings.ACCESS_TOKEN_SUBJECT
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")


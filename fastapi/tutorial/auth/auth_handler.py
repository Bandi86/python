from datetime import datetime, timedelta
from typing import Union
from fastapi import Depends, HTTPException, status
from jose import jwt
from fastapi.security import OAuth2PasswordBearer

oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")
SECRET_KEY = "bce3840ab4ef7a9b96c5eb3a1fbe22e57fe8a7b6ac129cc301b7f85653cb20da"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# data = {"email" : user_email}
def create_acces_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode_data = data.copy()
    if expires_delta:
        expires = datetime.utcnow() + expires_delta
    else:
        expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode_data.update({"exp" : expires})        
    # create acces token:
    encode_jwt = jwt.encode(to_encode_data, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

def is_token_valid(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        expire = payload.get("exp")
        if expire:
            if expire < datetime.timestamp(datetime.utcnow()):
                return False
            else:
                return True
        else:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                detail="could not find expire",
                headers={"WWW-Authenticate": "Bearer"},
                )
    except:
        raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                detail="could not find expire",
                headers={"WWW-Authenticate": "Bearer"},
                )

def extract_email_from_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        email = payload.get("email")
        if email is None:
             raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                detail="could not find email in token",
                headers={"WWW-Authenticate": "Bearer"},
                )
    except:
          raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                detail="could not find email in token",
                headers={"WWW-Authenticate": "Bearer"},
                )
          
    return email      
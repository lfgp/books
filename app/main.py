from fastapi import FastAPI
import os
from dotenv import load_dotenv
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm 

load_dotenv()

secret_key = os.getenv("SECRET_KEY")
algorithm = os.getenv("ALGORITHM")
access_token_expire_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

from app.auth_routes import auth_router
from app.books_routes import book_router

app.include_router(auth_router)
app.include_router(book_router)
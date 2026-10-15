from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import engine
from sqlalchemy.orm import sessionmaker
from app.models import User, db

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/login")
async def login():
    return {"message": "Login endpoint"}

@auth_router.post("/register")
async def register(email: str, password: str):
    Session = sessionmaker(bind=db)
    session = Session()
    existing_user = session.query(User).filter_by(email=email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")
    new_user = User(email=email, password=password)
    session.add(new_user)
    session.commit()
    return {"message": "Account registered successfully"}
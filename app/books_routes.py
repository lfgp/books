from fastapi import APIRouter, Depends, HTTPException, status

book_router = APIRouter(prefix="/books", tags=["books"])

@book_router.get("/list")
async def list_books():
    return {"message": "List of books"}         
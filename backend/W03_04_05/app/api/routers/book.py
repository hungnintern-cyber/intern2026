from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.book import BookCreate, BookUpdate, BookResponse
from app.services import book_service
from app.api.deps import get_current_user, get_current_admin_user

router = APIRouter()

@router.get("/", response_model=List[BookResponse])
def read_books(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, gt=0),
    db: Session = Depends(get_db)
):
    return book_service.get_books(db, skip=skip, limit=limit)

@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(
    book_in: BookCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return book_service.create_book(db, book_in, user_id=current_user.id)

@router.get("/{book_id}", response_model=BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    return book_service.get_book(db, book_id)

@router.put("/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int, 
    book_in: BookUpdate, 
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return book_service.update_book(db, book_id, book_in, current_user)

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(
    book_id: int,
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin_user)
):
    book_service.delete_book(db, book_id)
    return None
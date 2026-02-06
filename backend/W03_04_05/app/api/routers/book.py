from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.database import get_db
from app.schemas.book import BookCreate, BookUpdate, BookResponse
from app.services import book_service
from app.api.deps import get_current_user, get_current_admin_user

router = APIRouter()

@router.get("/", response_model=List[BookResponse])
def read_books(
    skip: Optional[int] = Query(None, ge=0),
    limit: Optional[int] = Query(None, gt=0),
    db: Session = Depends(get_db)
):
    return book_service.get_books(db, skip=skip, limit=limit)

@router.post("/", response_model=BookResponse, status_code=201)
def create_book(
    book_in: BookCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return book_service.create_book(db, book_in, user_id=current_user.id)

@router.get("/books/{book_id}", response_model=BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = book_service.get_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy")
    return db_book

@router.put("/books/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int, 
    book_in: BookUpdate, 
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    db_book = book_service.get_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy")
    if current_user.role != "admin" and db_book.owner_id != current_user.id:
        raise HTTPException(
            status_code=403, 
            detail="Không được phép sửa sách của người khác"
        )
    return book_service.update_book(db, db_book, book_in)

@router.delete("/books/{book_id}", status_code=204)
def delete_book(
    book_id: int,
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin_user)
):
    db_book = book_service.get_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy")
    
    book_service.delete_book(db, db_book)
    return None
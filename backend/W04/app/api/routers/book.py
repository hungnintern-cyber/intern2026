from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.book import BookCreate, BookUpdate, BookResponse
from app.services import book_service
from typing import Optional

# tạo router (tạo 1 nhóm API)
router = APIRouter()

# hàm lấy danh sách có phân trang skip, limit
@router.get("/books/", response_model=List[BookResponse])
def read_books(
    skip: Optional[int] = Query(None, ge=0), # không truyền -> skip = None, có truyền -> phải >= 0
    limit: Optional[int] = Query(None, gt=0),# không truyền -> limit = None, có truyền -> phải > 0
    db: Session = Depends(get_db)
):
    return book_service.get_books(db, skip=skip, limit=limit)

# hàm tạo mới
# 201: tạo thành công
@router.post("/books/", response_model=BookResponse, status_code=201)
# product_in: dữ liệu gửi từ client (JSON), FastAPI tự convert sang ProductCreate
def create_book(book_in: BookCreate, db: Session = Depends(get_db)):
    return book_service.create_book(db, book_in)

# lấy chi tiết
@router.get("/books/{book_id}", response_model=BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = book_service.get_book(db, book_id)
    # không tìm thấy thì trả lỗi chuẩn REST
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

# cập nhật
# có thể gửi 1 phần, ko gửi field nào thì field đó ko đổi
@router.put("/books/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int, 
    book_in: BookUpdate, 
    db: Session = Depends(get_db)
):
    db_book = book_service.get_book(db, book_id)
    # không tìm thấy thì trả lỗi chuẩn REST
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # logic update nằm ở Service
    return book_service.update_book(db, db_book, book_in)

# xóa
# 204: thành công nhưng không trả body
@router.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = book_service.get_book(db, book_id)
    # không tìm thấy thì trả lỗi chuẩn REST
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # nếu có thì xóa
    book_service.delete_book(db, db_book)
    return None
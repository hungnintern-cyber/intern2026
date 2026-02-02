from sqlalchemy.orm import Session
from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate
from typing import Optional

# lấy danh sách có phân trang skip,limit
def get_books(db: Session, skip: int = 0, limit: int = 10):
    query = db.query(Book)
    # chỉ phân trang khi client truyền skip & limit
    if skip is not None and limit is not None:
        query = query.offset(skip).limit(limit)
    return query.all()

# lấy chi tiết
def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

# hàm tạo mới
def create_book(db: Session, book_in: BookCreate):
    db_book = Book(**book_in.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# cập nhật
def update_book(db: Session, db_book: Book, book_in: BookUpdate):
    update_data = book_in.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_book, key, value)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# xóa 
def delete_book(db: Session, db_book: Book):
    db.delete(db_book)
    db.commit()
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.book import Book
from app.models.user import UserRole
from app.schemas.book import BookCreate, BookUpdate

def get_books(db: Session, skip: int = 0, limit: int = 10):
    query = db.query(Book)
    if skip is not None and limit is not None:
        query = query.offset(skip).limit(limit)
    return query.all()

def get_book(db: Session, book_id: int):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Không tìm thấy sách"
        )
    return db_book

def create_book(db: Session, book_in: BookCreate, user_id: int):
    db_book = Book(
        **book_in.model_dump(),
        owner_id=user_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book_id: int, book_in: BookUpdate, current_user):
    db_book = get_book(db, book_id)
    if current_user.role != UserRole.ADMIN and db_book.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Không có quyền sửa sách này"
            )
    update_data = book_in.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_book, key, value)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
 
def delete_book(db: Session, book_id: int):
    db_book = get_book(db, book_id)

    db.delete(db_book)
    db.commit()
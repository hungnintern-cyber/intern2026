# kiểu dữ liệu của cột trong database
from sqlalchemy import Column, Integer, String, Float, Date
# Base là class cha
from app.db.database import Base

# tạo model Book, 1 class là 1 bảng trong database
class Book(Base):
    __tablename__ = "books" # tên bảng trong Database
    # số nguyên, khóa chính ko trùng ko null tự tăng, index tìm nhanh
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    published_date = Column(Date, nullable=True) # ngày xuất bản có thể null
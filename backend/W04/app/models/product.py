# kiểu dữ liệu của cột trong database
from sqlalchemy import Column, Integer, String, Float, Boolean
# Base là class cha
from app.db.database import Base

# tạo model Product, 1 class là 1 bảng trong database
class Product(Base):
    __tablename__ = "products" # tên bảng trong Database
    # số nguyên, khóa chính ko trùng ko null tự tăng, index tìm nhanh
    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String, index=True) # kiểu chuỗi, index tìm nhanh
    price = Column(Float) # số thực
    # trang thái true -> hiển thị, false -> ẩn, mặc định true
    is_active = Column(Boolean, default=True)
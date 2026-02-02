# lớp gốc của Pydantic
from pydantic import BaseModel
# có thể có hoặc không
from typing import Optional

# khuôn mẫu cơ bản
class ProductBase(BaseModel):
    name: str
    price: float
    is_active: bool = True

# khuôn dùng để tạo
class ProductCreate(ProductBase):
    pass

# khuôn dùng để update
# các trường đều là Optional nên có thể chỉ update 1 field, không bắt buộc gửi đủ
class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    is_active: Optional[bool] = None

# khuôn dùng để trả về (có thêm ID)
class ProductResponse(ProductBase):
    id: int
    
    # from_attributes = True giúp Pydantic đọc hiểu được object của SQLAlchemy
    # đọc obj.id, obj.name thay vì chỉ đọc dict
    class Config:
        from_attributes = True
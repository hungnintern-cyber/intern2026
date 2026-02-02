from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import date

# khuôn mẫu cơ bản
class BookBase(BaseModel):
    title: str
    author: str
    price: float
    published_date: Optional[date] = None

# khuôn dùng để tạo (Validate giá > 0)
class BookCreate(BookBase):
    @field_validator('price')
    def check_price(cls, v):
        if v <= 0:
            raise ValueError('Giá sách phải lớn hơn 0')
        return v

# khuôn dùng để update
# các trường đều là Optional nên có thể chỉ update 1 field, không bắt buộc gửi đủ
class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    price: Optional[float] = None
    published_date: Optional[date] = None

# khuôn dùng để trả về (có thêm ID)
class BookResponse(BookBase):
    id: int
    class Config:
        from_attributes = True
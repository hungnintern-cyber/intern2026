from pydantic import BaseModel, field_validator, ConfigDict
from typing import Optional
from datetime import date

class BookBase(BaseModel):
    title: str
    author: str
    price: float
    published_date: Optional[date] = None

class BookCreate(BookBase):
    @field_validator('price')
    def check_price(cls, v):
        if v <= 0:
            raise ValueError('Giá sách phải lớn hơn 0')
        return v

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    price: Optional[float] = None
    published_date: Optional[date] = None
    @field_validator('price')
    def check_price(cls, v):
        if v is not None and v <= 0:
            raise ValueError('Giá sách cập nhật phải lớn hơn 0')
        return v

class BookResponse(BookBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
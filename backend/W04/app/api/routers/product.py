# APIRouter: tạo nhóm API (giống controller)
# Depends: dùng Dependency Injection (lấy DB session)
# HTTPException: trả lỗi HTTP (404, 400…)
# Query: validate query param (?min_price=...)
from fastapi import APIRouter, Depends, HTTPException, Query
# kiểu dữ liệu của db session
from sqlalchemy.orm import Session
# List trả về danh sách, Optional có cũng được, không có cũng được
from typing import List, Optional
# hàm quản lý session DB
from app.db.database import get_db
# các schema Pydantic nhận và trả dự liệu
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse
# Router không xử lý DB trực tiếp -> import Service
from app.services import product_service 

# tạo router (tạo 1 nhóm API)
router = APIRouter()

# hàm Lấy danh sách
@router.get("/products/", response_model=List[ProductResponse])
def read_products(
    # lấy từ query: /products/?min_price=100, Optional ko truyền cũng ok, gt=0 phải > 0
    min_price: Optional[float] = Query(None, gt=0),
    # gọi get_db() lấy db cho vào hàm xong request rồi đóng session
    db: Session = Depends(get_db)
):
    # Router chỉ gọi service, không đụng DB
    return product_service.get_products(db, min_price)

# hàm tạo mới
# 201: tạo thành công
@router.post("/products/", response_model=ProductResponse, status_code=201)
# product_in: dữ liệu gửi từ client (JSON), FastAPI tự convert sang ProductCreate
def create_product(product_in: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_product(db, product_in)

# lấy chi tiết
@router.get("/products/{product_id}", response_model=ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = product_service.get_product(db, product_id)
    # không tìm thấy thì trả lỗi chuẩn REST
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

# cập nhật
# có thể gửi 1 phần, ko gửi field nào thì field đó ko đổi
@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int, 
    product_in: ProductUpdate, 
    db: Session = Depends(get_db)
):
    db_product = product_service.get_product(db, product_id)
    # không tìm thấy thì trả lỗi chuẩn REST
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    # logic update nằm ở Service
    return product_service.update_product(db, db_product, product_in)

# xóa
# 204: thành công nhưng không trả body
@router.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = product_service.get_product(db, product_id)
    # không tìm thấy thì trả lỗi chuẩn REST
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product_service.delete_product(db, db_product)
    return None
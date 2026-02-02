# import FastAPI framework
from fastapi import FastAPI
# engine kết nối tới database
from app.db.session import engine
# class cha của tất cả Model
from app.db.database import Base
# import router product
from app.api.routers import product

# tạo bảng database (dùng Base của SQLAlchemy)
# SQLAlchemy sẽ quét tất cả class kế thừa Base
# lấy __tablename__, tạo bảng nếu CHƯA tồn tại
Base.metadata.create_all(bind=engine)

# tạo ứng dụng FastAPI
app = FastAPI()
# gắn toàn bộ API trong product.router vào app
app.include_router(product.router)

# API test nhanh
@app.get("/")
def root():
    return {"message": "Hello World"}
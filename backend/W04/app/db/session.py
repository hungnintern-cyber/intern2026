# engine là cổng kết nối tới database
from sqlalchemy import create_engine
# session là phiên làm việc với database, sessionmaker là máy tạo session
from sqlalchemy.orm import sessionmaker
# lấy DATABASE_URL từ config
from app.core.config import settings

# tạo engine
# settings.DATABASE_URL địa chỉ database sqlite:///./database.db
# check_same_thread=False: cho phép nhiều luồng dùng chung database
# vì SQLite mặc định chỉ cho phép 1 thread (luồng) truy cập database
# và FastAPI / Web API chạy nhiều request cùng lúc
# engine quản lý kết nối database
engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})

# tạo SessionLocal
# SessionLocal là class để tạo session, mỗi request sẽ tạo 1 session riêng
# autocommit=False không tự động lưu vào database
# autoflush=False không tự động đẩy dữ liệu tạm xuống DB
#bind=engine gắn session này với engine ở trên
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
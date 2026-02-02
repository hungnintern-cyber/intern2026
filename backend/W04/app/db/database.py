# declarative_base là hàm tạo ra Base class cho SQLAlchemy
# Base sẽ là cha của tất cả model (table)
from sqlalchemy.ext.declarative import declarative_base
# import máy tạo session từ session
from app.db.session import SessionLocal

# tạo Base
Base = declarative_base()

# hàm Dependency (Để các Router mượn kết nối DB)
# mỗi khi có Request vào, nó mở ra 1 session. Xử lý xong, nó tự đóng lại (db.close).
def get_db(): # hàm quản lý phiên
    # tạo 1 session làm việc với database
    db = SessionLocal()
    try:
        yield db # trả db cho router sử dụng, cho phép chạy code phía sau khi API xong
    finally:
        db.close() # luôn đóng session, kể cả khi API lỗi, exception xảy ra
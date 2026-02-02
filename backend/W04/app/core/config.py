# thư viện dùng để làm việc với hệ điều hành, đặc biệt là biến môi trường
import os
# class dùng để chứa các cấu hình của project
class Settings:
    # lấy đường dẫn DB từ biến môi trường DATABASE_URL, nếu không có thì dùng mặc định
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./database.db")

# tạo object từ class Settings
settings = Settings()
import enum
from sqlalchemy import Column, Integer, String, Boolean, Enum as DbEnum
from app.db.database import Base

class UserRole(str, enum.Enum):
    USER = "user"
    ADMIN = "admin"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(DbEnum(UserRole), default=UserRole.USER)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
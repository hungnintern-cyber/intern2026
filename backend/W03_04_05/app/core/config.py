import os
class Settings:
    PROJECT_NAME: str = "hungn_intern_2026"
    PROJECT_VERSION: str = "0.1.0"
    DATABASE_URL: str = "sqlite:///./database.db"
    SECRET_KEY: str = "hungn_intern_2026"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()
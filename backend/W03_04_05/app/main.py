from fastapi import FastAPI
from app.db.session import engine
from app.db.database import Base
from app.api.routers import product, book, auth, user
from app.core.config import settings

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(book.router, prefix="/books", tags=["Books"])
app.include_router(product.router, prefix="/products", tags=["Products"])

@app.get("/", tags=["Health Check"])
def root():
    return {"message": "Hello World"}
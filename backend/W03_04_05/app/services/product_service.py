from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate

def get_products(db: Session, min_price: float = None):
    query = db.query(Product)
    if min_price:
        query = query.filter(Product.price >= min_price)
    return query.all()

def create_product(db: Session, product_in: ProductCreate):
    db_product = Product(**product_in.model_dump())
    
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Product not found"
        )
    return db_product

def update_product(db: Session, product_id: int, product_in: ProductUpdate):
    db_product = get_product(db, product_id)
    update_data = product_in.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_product, key, value)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    db.delete(db_product)
    db.commit()
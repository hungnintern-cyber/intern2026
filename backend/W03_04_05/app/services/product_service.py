from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate

def get_products(db: Session, min_price: float = None):
    query = db.query(Product)
    if min_price:
        query = query.filter(Product.price >= min_price)
    return query.all()

def create_product(db: Session, product_in: ProductCreate):
    db_product = Product(name=product_in.name, price=product_in.price, is_active=product_in.is_active)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def update_product(db: Session, db_product: Product, product_in: ProductUpdate):
    update_data = product_in.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(db_product, key, value)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, db_product: Product):
    db.delete(db_product)
    db.commit()
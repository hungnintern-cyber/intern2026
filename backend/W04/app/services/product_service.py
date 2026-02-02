# phiên làm việc với database, mượn từ get_db() truyền vào
from sqlalchemy.orm import Session
# Model SQLAlchemy -> đại diện bảng products
from app.models.product import Product
# Schema Pydantic tạo, cập nhật
from app.schemas.product import ProductCreate, ProductUpdate

# hàm Lấy danh sách
# db: session database, min_price: giá tối thiểu (không bắt buộc)
def get_products(db: Session, min_price: float = None):
    query = db.query(Product) # SELECT * FROM products
    if min_price:
        query = query.filter(Product.price >= min_price) # WHERE price >= min_price
    return query.all() # chạy câu lệnh

# hàm tạo mới
# product_in: dữ liệu user gửi lên Pydantic
def create_product(db: Session, product_in: ProductCreate):
    # chuyển từ Schema (Pydantic) sang Model (SQLAlchemy)
    # Pydantic không lưu DB, SQLAlchemy mới lưu DB
    db_product = Product(name=product_in.name, price=product_in.price, is_active=product_in.is_active)
    db.add(db_product)      # thêm vào phiên làm việc
    db.commit()             # lưu vào DB
    db.refresh(db_product)  # lấy lại ID vừa tạo
    return db_product       # trả về object

# lấy chi tiết
def get_product(db: Session, product_id: int):
    # SELECT * FROM products WHERE id = ? LIMIT 1
    return db.query(Product).filter(Product.id == product_id).first()

# cập nhật
# db_product: sản phẩm cũ (đã lấy từ DB), product_in: dữ liệu mới (có thể thiếu field)
def update_product(db: Session, db_product: Product, product_in: ProductUpdate):
    # chỉ lấy những trường user có gửi lên (loại bỏ cái None)
    update_data = product_in.dict(exclude_unset=True)
    
    # gán giá trị mới vào object cũ
    for key, value in update_data.items():
        setattr(db_product, key, value)
    # lưu lại
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# xóa 
def delete_product(db: Session, db_product: Product):
    # DELETE FROM products WHERE id = ?
    db.delete(db_product)
    db.commit()
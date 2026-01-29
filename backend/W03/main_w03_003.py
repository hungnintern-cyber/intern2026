from typing import Optional
from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select

# dùng SQLModel để vừa validate vừa làm bảng (table=True)
class Product(SQLModel, table=True):
    # id có thể là None lúc đầu (để DB tự sinh số 1, 2, 3...)
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(min_length=1)  # validate: name không được rỗng
    price: float = Field(gt=0)       # validate: price > 0
    is_active: bool = True           # mặc định là True

# kết nối đến file database.db
engine = create_engine("sqlite:///database.db")

app = FastAPI()

# khi Server bật tự động tạo bảng trong DB
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

# API lưu vào DB
@app.post("/products/")
def create_product(product: Product):
    with Session(engine) as session:
        session.add(product)     # thêm vào
        session.commit()         # lưu xuống
        session.refresh(product) # lấy lại ID vừa sinh
        return product

# API Xem danh sách lấy từ DB ra
@app.get("/products/")
def read_products():
    with Session(engine) as session:
        # SELECT * FROM product
        products = session.exec(select(Product)).all()
        return products
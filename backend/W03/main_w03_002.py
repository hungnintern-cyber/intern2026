from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# tạo schema
class Product(BaseModel):
    id: int
    name: str = Field(min_length=1)  # validate: name không được rỗng
    price: float = Field(gt=0)       # validate: price > 0
    is_active: bool = True           # mặc định là True

# API tạo sản phẩm
@app.post("/products/") # đăng ký địa chỉ để gửi dữ liệu lên (REST Theory)
def create_product(product: Product): # dữ liệu gửi lên phải đúng khuôn mẫu Product (Pydantic Schema)
    return {"message": "Thêm thành công", "data": product}

# API Lấy sản phẩm theo ID (Path Parameter)
@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {"product_id": product_id}

# API tìm kiếm (Query Parameter)
@app.get("/search")
def search_product(keyword: str):
    return {"result": keyword}
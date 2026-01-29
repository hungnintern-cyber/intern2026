from fastapi import FastAPI

# khởi tạo ứng dụng
app = FastAPI()
# tạo endpoint
@app.get("/")
async def read_root():
    return {"Hello": "World"}

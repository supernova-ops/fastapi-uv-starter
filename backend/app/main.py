# main.py
from fastapi import FastAPI
from typing import List

# 🔥 핵심: 같은 폴더에 있는 schemas.py에서 클래스들을 가져옵니다.
from schemas import ItemCreate, ItemResponse

app = FastAPI(title="Pydantic 분리 예제")

# 임시 데이터베이스
fake_items_db = []

@app.get("/")
def read_root():
    return {"message": "파일을 분리하니 코드가 훨씬 깔끔해졌죠?"}

# [POST] 상품 등록
@app.post("/items/", response_model=ItemResponse, status_code=201)
def create_item(item: ItemCreate):
    # 로직은 그대로지만, ItemCreate가 무엇인지는 schemas.py에 정의되어 있습니다.
    new_id = len(fake_items_db) + 1
    saved_item = ItemResponse(id=new_id, **item.model_dump())
    fake_items_db.append(saved_item)
    return saved_item

# [GET] 전체 상품 조회
@app.get("/items/", response_model=List[ItemResponse])
def read_items():
    return fake_items_db
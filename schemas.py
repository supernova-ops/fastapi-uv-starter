# schemas.py
from pydantic import BaseModel, Field
from typing import Optional, List

# ==========================================
# 🧱 데이터 모델 정의 (여기서만 관리합니다)
# ==========================================

class ItemCreate(BaseModel):
    name: str = Field(..., min_length=2, example="맥북 프로")
    price: float = Field(..., gt=0, example=199.99)
    description: Optional[str] = Field(None, example="가볍고 강력한 노트북")
    tags: List[str] = Field(default_factory=list, example=["Apple", "Laptop"])

class ItemResponse(ItemCreate):
    id: int
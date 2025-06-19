from pydantic import BaseModel
from typing import Optional

class FavoriteBase(BaseModel):
    product_id: int
    title: str
    image: str
    price: float
    rating: Optional[float] = None

class FavoriteCreateInput(BaseModel):
    product_id: int

class FavoriteOutput(FavoriteBase):
    id: int

    model_config = {
        "from_attributes": True
    }
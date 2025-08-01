from pydantic import BaseModel
from typing import List, Optional

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: Optional[float] = None
    tags: List[str] = []
    out_of_stock: bool = False
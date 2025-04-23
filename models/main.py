from pydantic import BaseModel, Field

class Product(BaseModel):
    id: int
    name: str
    price: float
    description: str

class CartItem(BaseModel):
    product_id: int
    name: str
    quantity: int = Field(..., ge=1, description="Quantity must be greater than 0")
    price: float

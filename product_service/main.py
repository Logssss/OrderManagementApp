from fastapi import APIRouter, HTTPException, status
from models.main import Product

router = APIRouter()

# Dummy product list (this can be replaced with an actual database)
products = [
    Product(id=1, name="Apple", price=1.2, description="Fresh apple"),
    Product(id=2, name="Banana", price=0.5, description="Sweet banana"),
    Product(id=3, name="Carrot", price=0.7, description="Organic carrot"),
]

@router.get("/list", response_model=list[Product], status_code=status.HTTP_200_OK)
def get_products():
    return products

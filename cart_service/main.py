from fastapi import APIRouter, HTTPException, status
from models.main import CartItem
from db.main import cart_db

router = APIRouter()

@router.post("/add", status_code=status.HTTP_201_CREATED)
def add_to_cart(item: CartItem):
    if not item.product_id or item.quantity <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid item data")
    cart_db.append(item)
    return {"message": "Item added to cart", "item": item}

@router.get("/view", response_model=list[CartItem], status_code=status.HTTP_200_OK)
def view_cart():
    if not cart_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart is empty")
    return cart_db

@router.post("/clear", status_code=status.HTTP_200_OK)
def clear_cart():
    cart_db.clear()
    return {"message": "Cart cleared successfully"}

from fastapi import APIRouter, HTTPException, status
from db.main import cart_db, order_history
from models.main import CartItem

router = APIRouter()

@router.post("/place", status_code=status.HTTP_201_CREATED)
def place_order():
    if not cart_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cart is empty")
    order = {
        "id": len(order_history) + 1,
        "items": cart_db.copy(),
        "status": "Confirmed"
    }
    order_history.append(order)
    cart_db.clear()
    return {"message": "Order placed successfully", "order": order}

@router.get("/{order_id}", status_code=status.HTTP_200_OK)
def get_order(order_id: int):
    order = next((order for order in order_history if order["id"] == order_id), None)
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return order

@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: int):
    order = next((order for order in order_history if order["id"] == order_id), None)
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    order_history.remove(order)
    return {"message": "Order deleted successfully"}

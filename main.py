from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from product_service.main import router as product_router
from cart_service.main import router as cart_router
from order_service.main import router as order_router

app = FastAPI()

from fastapi.responses import RedirectResponse

@app.get("/")
async def root():
    return RedirectResponse(url="/static/index.html")

# Mount static HTML
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

# Include microservice routers
app.include_router(product_router, prefix="/product")
app.include_router(cart_router, prefix="/cart")
app.include_router(order_router, prefix="/order")

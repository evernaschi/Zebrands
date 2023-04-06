from fastapi import APIRouter
from app.api.api_v1.endpoints import products, users, login

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(products.router, prefix="/products", tags=["products"])
api_router.include_router(users.router, prefix="/users", tags=["users"])

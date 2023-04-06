from typing import Optional

from pydantic import BaseModel


# Shared properties
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    sku: str
    price: float
    brand: str


# Properties to receive on Product creation
class ProductCreate(ProductBase):
    name: str


# Properties to receive on Product update
class ProductUpdate(ProductBase):
    pass


# Properties shared by models stored in DB
class ProductInDBBase(ProductBase):
    name: str
    id: int
    owner_id: int
    sku: str
    price: float
    brand: str

    class Config:
        orm_mode = True


# Properties to return to client
class Product(ProductInDBBase):
    pass


# Properties properties stored in DB
class ProductInDB(ProductInDBBase):
    queries: int

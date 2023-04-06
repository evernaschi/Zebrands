from sqlalchemy import Column, ForeignKey, Integer, Float, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Product(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    sku = Column(String, index=True)
    brand = Column(String, index=True)
    price = Column(Float)
    queries = Column(Integer, default=0)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="products")

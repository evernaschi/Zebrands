import random
from typing import Optional

from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.products import ProductCreate
from app.tests.utils.users import create_random_user
from app.tests.utils.utils import random_lower_string


def create_random_product(
    db: Session, *, owner_id: Optional[int] = None
) -> models.Product:
    if owner_id is None:
        user = create_random_user(db)
        owner_id = user.id
    sku = random_lower_string()
    name = random_lower_string()
    price = random.uniform(1, 100)
    brand = random_lower_string()
    product_in = ProductCreate(sku=sku, name=name, price=price, brand=brand, id=id)
    return crud.product.create_with_owner(db=db, obj_in=product_in, owner_id=owner_id)

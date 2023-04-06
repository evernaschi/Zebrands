from sqlalchemy.orm import Session
import random

from app import crud
from app.schemas.products import ProductCreate, ProductUpdate
from app.tests.utils.users import create_random_user
from app.tests.utils.utils import random_lower_string


def test_create_product(db: Session) -> None:
    sku = random_lower_string()
    name = random_lower_string()
    brand = random_lower_string()
    price = random.uniform(1, 100)
    product_in = ProductCreate(name=name, sku=sku, brand=brand, price=price)
    user = create_random_user(db)
    product = crud.product.create_with_owner(db=db, obj_in=product_in, owner_id=user.id)
    assert product.sku == sku
    assert product.price == price
    assert product.brand == brand
    assert product.owner_id == user.id


def test_get_product(db: Session) -> None:
    sku = random_lower_string()
    name = random_lower_string()
    brand = random_lower_string()
    price = random.uniform(1, 100)
    product_in = ProductCreate(name=name, sku=sku, brand=brand, price=price)
    user = create_random_user(db)
    product = crud.product.create_with_owner(db=db, obj_in=product_in, owner_id=user.id)
    stored_product = crud.product.get(db=db, id=product.id)
    assert stored_product
    assert product.id == stored_product.id
    assert product.price == stored_product.price
    assert product.sku == stored_product.sku
    assert product.brand == stored_product.brand
    assert product.owner_id == stored_product.owner_id


def test_update_product(db: Session) -> None:
    sku = random_lower_string()
    name = random_lower_string()
    brand = random_lower_string()
    price = random.uniform(1, 100)
    product_in = ProductCreate(name=name, sku=sku, brand=brand, price=price)
    user = create_random_user(db)
    product = crud.product.create_with_owner(db=db, obj_in=product_in, owner_id=user.id)
    brand2 = random_lower_string()
    product_update = ProductUpdate(name=name, sku=sku, brand=brand2, price=price)
    product2 = crud.product.update(db=db, db_obj=product, obj_in=product_update)
    assert product.id == product2.id
    assert product.price == product2.price
    assert product.sku == product2.sku
    assert product2.brand == brand2
    assert product.owner_id == product2.owner_id


def test_delete_product(db: Session) -> None:
    sku = random_lower_string()
    name = random_lower_string()
    brand = random_lower_string()
    price = random.uniform(1, 100)
    product_in = ProductCreate(name=name, sku=sku, brand=brand, price=price)
    user = create_random_user(db)
    product = crud.product.create_with_owner(db=db, obj_in=product_in, owner_id=user.id)
    product2 = crud.product.remove(db=db, id=product.id)
    product3 = crud.product.get(db=db, id=product.id)
    assert product3 is None
    assert product2.id == product.id
    assert product2.price == product.price
    assert product2.sku == sku
    assert product2.brand == brand
    assert product2.owner_id == user.id

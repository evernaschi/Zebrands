from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.products import create_random_product


def test_create_product(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    data = {
        "sku": "999",
        "name": "Fighters",
        "price": 10.0,
        "brand": "Foo",
    }
    response = client.post(
        f"{settings.API_V1_STR}/products/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["sku"] == data["sku"]
    assert content["name"] == data["name"]
    assert content["price"] == data["price"]
    assert content["brand"] == data["brand"]
    assert "id" in content
    assert "owner_id" in content


def test_read_product(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    product = create_random_product(db)
    response = client.get(
        f"{settings.API_V1_STR}/products/{product.id}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["sku"] == product.sku
    assert content["name"] == product.name
    assert content["price"] == product.price
    assert content["brand"] == product.brand
    assert content["id"] == product.id
    assert content["owner_id"] == product.owner_id

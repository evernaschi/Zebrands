from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings
from app.db.base_class import Base  # noqa: F401
from app.db.session import SessionLocal, engine  # noqa: F401

init_products = [
    {
        "sku": "1234",
        "name": "Product 1",
        "price": 10.0,
        "brand": "Brand 1",
        "queries": 0,
    },
    {
        "sku": "5678",
        "name": "Product 2",
        "price": 20.0,
        "brand": "Brand 2",
        "queries": 0,
    },
]


def init_db(db: Session) -> None:
    # pylint: disable=invalid-name
    Base.metadata.create_all(bind=engine)

    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.user.create(db, obj_in=user_in)  # noqa: F841
    products = crud.product.get_multi(db)
    if not products:
        for product in init_products:
            product_in = schemas.ProductCreate(**product)
            crud.product.create_with_owner(db, obj_in=product_in, owner_id=user.id)


init_db(db=SessionLocal())

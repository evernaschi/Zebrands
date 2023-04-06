from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.utils import send_product_updated_email

router = APIRouter()


@router.get("/", response_model=List[schemas.Product])
def read_products(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve products.
    """
    products = crud.product.get_multi(db, skip=skip, limit=limit)
    return products


@router.post("/", response_model=schemas.Product)
def create_product(
    *,
    db: Session = Depends(deps.get_db),
    product_in: schemas.ProductCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new product.
    """
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    product = crud.product.create_with_owner(
        db=db, obj_in=product_in, owner_id=current_user.id
    )
    return product


@router.put("/{id}", response_model=schemas.Product)
def update_product(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    product_in: schemas.ProductUpdate,
    background_tasks: BackgroundTasks,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a product.
    """
    product = crud.product.get(db=db, id=id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if not crud.user.is_superuser(current_user) and (
        product.owner_id != current_user.id
    ):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    product = crud.product.update(db=db, db_obj=product, obj_in=product_in)
    background_tasks.add_task(send_product_updated_email, product.sku)
    return product


@router.get("/{id}", response_model=schemas.Product)
def read_product(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_user_or_anonymous),
) -> Any:
    """
    Get product by ID.
    """
    product = crud.product.get(db=db, id=id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if not current_user:
        crud.product.increment_queries(db=db, id=id)
    return product


@router.delete("/{id}", response_model=schemas.Product)
def delete_product(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete a product.
    """
    product = crud.product.get(db=db, id=id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    product = crud.product.remove(db=db, id=id)
    return product

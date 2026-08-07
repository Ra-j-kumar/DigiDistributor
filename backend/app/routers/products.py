from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import get_db

router = APIRouter(prefix="/api/products", tags=["Products"])

@router.post("/", response_model=schemas.ProductOut)
def add_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@router.get("/", response_model=list[schemas.ProductOut])
def list_products(db: Session = Depends(get_db)):
    return crud.get_products(db)

@router.get("/{product_id}", response_model=schemas.ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=schemas.ProductOut)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    updated_product = crud.update_product(db, product_id, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    deleted_product = crud.delete_product(db, product_id)
    if not deleted_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}
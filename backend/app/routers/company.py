from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud,schemas
from ..database import get_db

router = APIRouter(prefix="/api/company",tags=["Company"])

@router.get("/", response_model=schemas.CompanyOut)
def get_company(db: Session = Depends(get_db)):
    return crud.get_company(db)


@router.put("/", response_model=schemas.CompanyOut)
def update_company(data: schemas.CompanyUpdate, db: Session = Depends(get_db)):
    return crud.update_company(db, data)

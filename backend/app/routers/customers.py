from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from .. import schemas,crud
from ..database import get_db

router = APIRouter(prefix="/api/customers",tags=["customers"])

@router.post("/",response_model=schemas.CustomerOut)
def add_customer(customer:schemas.CustomerCreate,db:Session=Depends(get_db)):
    return crud.create_customer(db,customer)

@router.get("/",response_model=list[schemas.CustomerOut])
def list_customer(db:Session=Depends(get_db)):
    return crud.get_customers(db)

@router.get("/{customer_id}",response_model=schemas.CustomerOut)
def get_customer(customer_id:int,db:Session=Depends(get_db)):
    customer = crud.get_customer(db,customer_id)
    if not customer:
        raise HTTPException(status_code=404,detail="Customer not found")
    return customer       
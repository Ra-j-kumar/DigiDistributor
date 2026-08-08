# Data validation
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#------client Detail---------
class CompanyUpdate(BaseModel):
    name:str
    address : Optional[str] = None
    mobile : Optional[str] = None
    gstin : Optional[str] = None
    fssai_no : Optional[str] = None
    fssai_valid_from : Optional[str] = None
    fssai_valid_to : Optional[str] = None
    jurisdiction_text : Optional[str] = "Subject To Local Jurisdiction."
    
class CompanyOut(CompanyUpdate):
    id: int

    class Config:
        from_attributes = True

#------customer---------
class CustomerCreate(BaseModel):
    name: str
    shop_name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    state: Optional[str] = None
    state_code: Optional[str] = None
    gstin: Optional[str] = None

class CustomerOut(CustomerCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

#------product---------
class ProductCreate(BaseModel):
    name: str
    category: Optional[str] = None
    hsn_code: Optional[str] = None
    unit: str = "pcs"
    mrp: Optional[float] = None
    price_per_unit: Optional[float] = None
    gst_rate: float = 5.0
    stock_quantity: float = 0

class ProductOut(ProductCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
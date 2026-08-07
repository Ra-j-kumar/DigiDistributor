# Data validation
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

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
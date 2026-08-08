from .database import Base
from sqlalchemy import Column , Integer, String, Float, DateTime , func

class Company(Base):
    __tablename__ = "company"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String, nullable=False, default="Your Company Name")
    address = Column(String, nullable=False)
    mobile = Column(String, nullable=False)
    gstin = Column(String, nullable=False)
    fssai_no = Column(String, nullable=False)
    fssai_valid_from = Column(String, nullable=False)   # stored as plain text e.g. "02-10-2022"
    fssai_valid_to = Column(String, nullable=False)
    jurisdiction_text = Column(String, default="Subject To Local Jurisdiction.")

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
    shop_name = Column(String,nullable=False)
    phone = Column(String,nullable=False)
    email = Column(String,nullable=False)
    address = Column(String,nullable=False)
    state = Column(String,nullable=False)
    state_code = Column(String,nullable=False)
    gstin = Column(String,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
    category = Column(String,nullable=False)
    hsn_code = Column(String,nullable=False)
    unit = Column(String,nullable=False)
    mrp = Column(Float,nullable=False)
    price_per_unit = Column(Float,nullable=False)
    gst_rate = Column(Float,default=5.0)
    stock_quantity = Column(Float,default=0)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
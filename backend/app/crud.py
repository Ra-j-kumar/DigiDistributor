from sqlalchemy.orm import Session
from . import models,schemas

# ---------- Company ----------
def get_company(db: Session):
    company = db.query(models.Company).filter(models.Company.id == 1).first()
    if not company:
        company = models.Company(
            id=1,
            name="Your Company Name",
            address="",
            mobile="",
            gstin="",
            fssai_no="",
            fssai_valid_from="",
            fssai_valid_to="",
            jurisdiction_text="Subject To Local Jurisdiction."
        )
        db.add(company)
        db.commit()
        db.refresh(company)

    return company

def update_company(db: Session, data: schemas.CompanyUpdate):
    company = get_company(db)
    for field, value in data.model_dump().items():
        setattr(company, field, value)
    db.commit()
    db.refresh(company)
    return company

# ---------- Customers ----------
def create_customer(db:Session,customer:schemas.CustomerCreate):
    db_customer = models.Customer(**customer.model_dump())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_customers(db:Session):
    return db.query(models.Customer).order_by(models.Customer.id.desc()).all()

def get_customer(db:Session, customer_id:int):
    return db.query(models.Customer).filter(customer_id == models.Customer.id).first()

def update_customer(db:Session, customer_id:int,customer:schemas.CustomerCreate):
    db_customer = get_customer(db,customer_id)
    if not db_customer:
        return None
    
    update_data = customer.model_dump(exclude_unset=True)
    for field , value in update_data.items():
        setattr(db_customer,field,value)
        
    db.commit()
    db.refresh(db_customer)
    return db_customer
    
def delete_customer(db:Session,customer_id:int):
    db_customer = get_customer(db,customer_id)
    if not db_customer:
        return None
    db.delete(db_customer)
    db.commit()
    return db_customer
    
# ---------- Products ----------
def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session):
    return db.query(models.Product).order_by(models.Product.id.desc()).all()

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def update_product(db:Session,product_id:int,product:schemas.ProductCreate):
    db_product = get_product(db,product_id)
    if not db_product:
        return None
    update_data = product.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_product,field,value)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db:Session, product_id:int):
    db_product = get_product(db,product_id)
    if not db_product:
        return None
    
    db.delete(db_product)
    db.commit()
    return db_product
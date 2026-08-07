from sqlalchemy.orm import Session
from . import models,schemas

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
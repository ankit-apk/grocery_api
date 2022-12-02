from sqlalchemy import Column, Integer, String, Float
from config import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    quantity_unit = Column(String)
    total_stock = Column(Integer)
    logo_image = Column(String)
    other_images = Column(String)
    description = Column(String)

from sqlalchemy import Column, Integer, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship

from app import db


# https://docs.sqlalchemy.org/en/latest/orm/self_referential.html
class Product(db.Model):
    id = Column(Integer(), primary_key=True)
    parent_id = Column(Integer(), ForeignKey('product.id'))
    published = Column(Boolean(), nullable=False, default=False)
    name = Column(Text(), nullable=False, default='Missing Item Name')
    stock = Column(Integer(), nullable=False, default=0)
    price = Column(Integer(), nullable=False, default=500)
    description = Column(Text(), nullable=False, default='No Description')
    notes_enabled = Column(Boolean(), nullable=False, default=True)
    variations = relationship('Product')

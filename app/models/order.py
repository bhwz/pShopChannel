from datetime import datetime
from sqlalchemy import Column, Integer, Boolean, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app import db


class Order(db.Model):
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('user.id'))
    product_id = Column(Integer(), ForeignKey('product.id'))
    state = Column(Integer(), nullable=False, default=-1)
    vendor_notes = Column(Text(), nullable=False, default='No notes.')
    customer_notes = Column(Text(), nullable=False, default='No custom order information was provided.')
    timestamp = Column(DateTime(), nullable=False, default=datetime.utcnow())
    user = relationship('User')
    product = relationship('Product')

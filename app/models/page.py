from sqlalchemy import Column, Integer, Boolean, Text, DateTime
from datetime import datetime

from app import db


class Page(db.Model):
    id = Column(Integer(), primary_key=True)
    published = Column(Boolean(), nullable=False, default=False)
    slug = Column(Text(), nullable=False, unique=True)
    title = Column(Text(), nullable=False, default='No Title')
    content = Column(Text(), nullable=False, default='No Content')
    timestamp = Column(DateTime(), nullable=False, default=datetime.utcnow())

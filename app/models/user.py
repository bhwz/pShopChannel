from datetime import datetime
from flask_login import UserMixin
from passlib.hash import argon2
from sqlalchemy import Column, Integer, String, Boolean, DateTime

from app import db, login


@login.user_loader
def load_user(uid):
    return User.query.get(int(uid))


class User(db.Model, UserMixin):
    id = Column(Integer(), primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    admin = Column(Boolean(), default=False)
    timestamp = Column(DateTime(), nullable=False, default=datetime.utcnow())

    def set_password(self, password):
        self.password = argon2.hash(password)

    def verify_password(self, password):
        return argon2.verify(password, self.password)

from sqlalchemy import Column, String, Integer, Boolean
from model.base import Model

class User(Model):
    # __abstract__ = True

    __tablename__ = 'auth_user'

    id          = Column(Integer, name="id", primary_key=True)

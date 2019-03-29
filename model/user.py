from sqlalchemy import Column, String, Integer, Boolean
from model.base import Model
from mixins.timestamp import TimestampMixin

class User(Model):

    __abstract__ = True

    __tablename__ = 'auth_user'

    id          = Column(Integer, name="id", primary_key=True)
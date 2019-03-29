from sqlalchemy import Column, String, Boolean
from model.base import Model
from mixins.timestamp import TimestampMixin

class User(Model, TimestampMixin):
    __abstract__ = True

    __tablename__ = 'user'

    email       = Column(String(75))
    first_name  = Column(String(30))
    last_name   = Column(String(30))
    is_active   = Column(Boolean, unique=False, default=True)
    username    = Column(String(30), unique=True, nullable=False),
    password    = Column(String(128), nullable=False)
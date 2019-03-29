from sqlalchemy import Column, String, Boolean
from model.base import Model
from mixins.timestamp import TimestampMixin

class User(Model, TimestampMixin):
    email       = Column(String(75), 'email')
    first_name  = Column(String(30), 'first_name')
    last_name   = Column(String(30), 'last_name')
    is_active   = Column(Boolean, unique=False, default=True)
    username    = Column(String(30), unique=True, nullable=False),
    password    = Column(String(128), nullable=False)
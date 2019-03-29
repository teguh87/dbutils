from sqlalchemy import Column, String, Integer, Boolean
from model.base import Model
from mixins.timestamp import TimestampMixin

class User(Model):

    __abstract__ = True

    __tablename__ = 'user'

    id          = Column(Integer, name="id", primary_key=True)
    email       = Column(String(75))
    first_name  = Column(String(30))
    last_name   = Column(String(30))
    is_active   = Column(Boolean, unique=False, default=True)
    username    = Column(String(30), unique=True, nullable=False),
    password    = Column(String(128), nullable=False)
    discriminator = Column(String(8))


    __mapper_args__ = {'polymorphic_on' : discriminator}
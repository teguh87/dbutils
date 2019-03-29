import uuid
from sqlalchemy import Column, String, Integer


class BaseMixin(object):
    __abstract__ = True

    id = Column(Integer, name="id", primary_key=True)
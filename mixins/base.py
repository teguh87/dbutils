import uuid
from sqlalchemy import Column, String

def generate_uuid():
    return str(uuid.uuid4())

class BaseMixin(object):
    __abstract__ = True

    id = Column(String, name="id", primary_key=True, default=generate_uuid)
import uuid
from abc import ABCMeta
from sqlalchemy import Column, String

def generate_uuid():
    return str(uuid.uuid4())

class BaseMixin(ABCMeta):
    id = Column(String, name="id", primary_key=True, default=generate_uuid)

from sqlalchemy import Column, String, Integer
from mixins.base import BaseMixin

class FileMixins(BaseMixin):
    filename = Column(String(120), name="filename", nullable=False)
    path = Column(String(255), name="path", nullable=False)
    size = Column(Integer(), name="size")

    def __repr__(self):
        pass

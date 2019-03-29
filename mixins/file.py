from mixins.timestamp import TimestampMixin
from sqlalchemy import Column, String, Integer

class FileMixins(TimestampMixin):
    filename = Column(String(120), name="filename", nullable=False)
    path = Column(String(255), name="path", nullable=False)
    size = Column(Integer(), name="size")


    def __repr__((self):
        pass

import uuid
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm.interfaces import MapperExtension

class BaseExtension(MapperExtension):
    """Base entension class for all entities """

    def before_insert(self, mapper, connection, instance):
        """ set the created_at  """
        instance.created_at = datetime.datetime.now()

    def before_update(self, mapper, connection, instance):
        """ set the updated_at  """
        instance.updated_at = datetime.datetime.now()

class BaseMixin(object):
    __abstract__ = True

    id = Column(Integer, name="id", primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    __mapper_args__ = { 'extension': BaseExtension() }

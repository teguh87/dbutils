from mixins.base import BaseMixin
from sqlalchemy import Column, DateTime

from sqlalchemy.orm.interfaces import MapperExtension

class BaseExtension(MapperExtension):
    """Base entension class for all entities """

    def before_insert(self, mapper, connection, instance):
        """ set the created_at  """
        instance.created_at = datetime.datetime.now()

    def before_update(self, mapper, connection, instance):
        """ set the updated_at  """
        instance.updated_at = datetime.datetime.now()

class TimestampMixin(BaseMixin):
    # _repr_hide = ['created_at', 'updated_at']

    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    __mapper_args__ = { 'extension': BaseExtension() }

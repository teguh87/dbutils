import uuid
from abc import ABCMeta
from sqlalchemy import Column, String


def generate_uuid():
    return str(uuid.uuid4())

class BaseMixin(ABCMeta):
    id = Column(String, name="id", primary_key=True, default=generate_uuid)

    @declared_attr
    def created_by_id(cls):
        return Column(Integer,
            ForeignKey('user.id', name='fk_%s_created_by_id' % cls.__name__, use_alter=True),
            # nullable=False,
            default=_current_user_id_or_none
        )

    @declared_attr
    def created_by(cls):
        return relationship(
            'User',
            primaryjoin='User.id == %s.created_by_id' % cls.__name__,
            remote_side='User.id'
        )

    @declared_attr
    def updated_by_id(cls):
        return Column(Integer,
            ForeignKey('user.id', name='fk_%s_updated_by_id' % cls.__name__, use_alter=True),
            # nullable=False,
            default=_current_user_id_or_none,
            onupdate=_current_user_id_or_none
        )

    @declared_attr
    def updated_by(cls):
        return relationship(
            'User',
            primaryjoin='User.id == %s.updated_by_id' % cls.__name__,
            remote_side='User.id'
        )

def _current_user_id_or_none():
    try:
        return current_user.id
    except:
        return None

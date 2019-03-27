"""SQLAlchemy Metadata and Session object"""
import datetime
import json
import time
from contextlib import contextmanager
from sqlalchemy import MetaData, event
from sqlalchemy.orm import scoped_session, sessionmaker


__all__ = ['Session', 'metadata', 'Model', 'SchemaEncoder']

# Remove expire_on_commit=False if autorefreshing of committed objects is
# desireable.
BaseSession = scoped_session(sessionmaker(expire_on_commit=False))
metadata = MetaData()

# Declarative base

from sqlalchemy.ext.declarative import declarative_base

class Session(BaseSession):
    def __init__(self, *a, **kw):
        super(Session, self).__init__(*a, **kw)
        self._in_atomic = False

    @contextmanager
    def atomic(self):
        """Transaction context manager.

        Will commit the transaction on successful completion
        of the block, or roll it back on error.

        Supports nested usage (via savepoints).

        """
        nested = self._in_atomic
        self.begin(nested=nested)
        self._in_atomic = True

        try:
            yield
        except:
            self.rollback()
            raise
        else:
            self.commit()
        finally:
            if not nested:
                self._in_atomic = False

class _Base(object):
    """ Metaclass for the Model base class."""
    # Only include these attributes when serializing using __json__. If
    # relationships should be serialized, then they need to be whitelisted.
    __json_whitelist__ = None

    @classmethod
    def get(cls, id):
        return Session.query(cls).get(id)

    @classmethod
    def get_by(cls, **kw):
        return Session.query(cls).filter_by(**kw).first()

    @classmethod
    @event.listens_for(Session, 'after_begin')
    def get_or_create(cls, **kw):
        r = cls.get_by(**kw)
        if r:
            return r

        return cls.create(**kw)

    @classmethod
    @event.listens_for(Session, 'after_begin')
    def create(cls, **kw):
        r = cls(**kw)
        Session.add(r)
        return r

    @classmethod
    @event.listens_for(Session, 'after_begin')
    def insert(cls, **kw):
        Session.execute(cls.__table__.insert(values=kw)).close()

    @classmethod
    def insert_many(cls, iter):
        Session.execute(cls.__table__.insert(), list(iter)).close()

    @classmethod
    def all(cls):
        return Session.query(cls).all()

    @classmethod
    def count(cls):
        return Session.query(cls).count()

    @event.listens_for(Session, 'after_begin')
    def delete(self):
        Session.delete(self)

    def refresh(self):
        Session.refresh(self)

    def __repr__(self):
        values = ', '.join("%s=%r" % (n, getattr(self, n)) for n in self.__table__.c.keys())
        return "%s(%s)" % (self.__class__.__name__, values)

    def __json__(self):
        if self.__json_whitelist__ is not None:
            return dict((k, getattr(self, k)) for k in self.__json_whitelist__)

        return dict((k, getattr(self, k)) for k in self.__table__.c.keys())


Model = declarative_base(metadata=metadata, cls=_Base)

class SchemaEncoder(json.JSONEncoder):
    """Encoder for converting Model objects into JSON."""

    def default(self, obj):
        if isinstance(obj, datetime.date):
            return time.strftime('%Y-%m-%dT%H:%M:%SZ', obj.utctimetuple())
        elif isinstance(obj, Model):
            return obj.__json__()
        return json.JSONEncoder.default(self, obj)

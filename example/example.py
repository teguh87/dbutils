import sys
import os
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

sys.path.append(os.path.join(os.path.dirname(__file__), '..')) 

from model.base import Model
from utils.db import connection
from mixins.base import BaseMixin
from model.user import User
from mixins.file import FileMixins

model = Model()

engine = connection(
    dbtype="postgresql",
    username= "example",
    password= "example123",
    dbhost="localhost",
    dbport="5432",
    dbname="example"
)

class Member(User):
    __tablename__= 'member'
    __mapper_args__={
        'polymorphic_identity':'member'
    }

def main():
    model.metadata.create_all(engine.make_connection())

if __name__=='__main__':
    main()


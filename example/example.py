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



def main():
    pass

if __name__=='__main__':
    pass


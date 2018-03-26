# coding=utf-8
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from base import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    features = relationship("Feature", back_populates="user")

    def __init__(self, name, birthday):
        self.name = name
        self.password = password
# coding=utf-8
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Feature(Base):
    __tablename__ = 'feature'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    target_date = Column(Date)
    client = Column(Integer)
    product_area = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="features")


    def __init__(self, title, description, priority, target_date, client, product_area, user):
        self.title = title
        self.description = description
        self.priority = priority
        self.target_date = target_date
        self.client = client
        self.product_area = product_area
        self.user = user
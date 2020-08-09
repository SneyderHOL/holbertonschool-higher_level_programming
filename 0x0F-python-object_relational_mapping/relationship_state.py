#!/usr/bin/python3
"""Module for State Class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State Class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          backref=backref("states",
                                          cascade="all, delete-orphan",
                                          single_parent=True))

#!/usr/bin/python3
"""Module for City Class"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """City Class"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'))
#    state = relationship("State")

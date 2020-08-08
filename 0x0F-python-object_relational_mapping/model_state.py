#!/usr/bin/python3
"""Module for State Class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()


class State(Base):
    """State Class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(128), nullable=False)

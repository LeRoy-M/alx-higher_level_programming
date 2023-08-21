#!/usr/bin/python3
"""Module that defines a class 'State' and an
instance 'Base = declarative_base()'
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class definition for 'State'"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))

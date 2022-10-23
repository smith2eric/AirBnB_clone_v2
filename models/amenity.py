#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = "amenities"
    __table_args__ = {"mysql_default_charset": "latin1"}
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)

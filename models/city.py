#!/usr/bin/python3
""" City Module for HBNB project """

from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship, backref
from os import getenv
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        state = relationship("State", backref="cities")

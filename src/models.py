import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    first_name = Column(String(250))
    last_name = Column(String(250))
    subscription_date = Column(DateTime)
    # Relación con favoritos
    favorites = relationship('Favorites', back_populates='user')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer)
    climate = Column(String(250))
    terrain = Column(String(250))
    population = Column(Integer)
    # Relación con favoritos
    favorites = relationship('Favorites', back_populates='planet')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
    # Relación con favoritos
    favorites = relationship('Favorites', back_populates='character')

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    
    # Relaciones!
    user = relationship('User', back_populates='favorites')
    planet = relationship('Planet', back_populates='favorites')
    character = relationship('Character', back_populates='favorites')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e
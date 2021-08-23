import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    username = Column(String(100))
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

class Favorites(Base):
    __tablename__ = 'Favorite'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    id_favorite = Column(Integer, nullable=False)
    type_favorite = Column(String(20), nullable=False)
    name = Column(String(100), nullable=False)
    user = relationship(User)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    climate = Column(String(40))
    gravity = Column(String(20))
    population = Column(Integer) 
    terrain = Column(String(40))
    surface_water = Column(Integer)
    diameter = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)     

class Person(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    birth_year = Column(Integer)
    gender = Column(String(6))
    eye_color = Column(String(15))
    height = Column(String(4))
    mass = Column(String(4))  
    home_world_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    race_id = Column(Integer, ForeignKey('race.id'))
    race = relationship(Race)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    vehicle = relationship(Vehicle)

class Species(Base):
    __tablename__ = 'specie'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    homeworld = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    languaje = Column(String(15))
    average_height = Column(Integer)
    average_lifespan = Column(Integer)
    classification = Column(String(50))
    designation = Column(String(50))
    eye_color = Column(String(15))
    hair_colors = Column(String(100))
    skin_colors = Column(String(100))
    

class Starships(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    model = Column(String(100))
    cost_in_credits = Column(Integer)
    max_atmosphering_speed = Column(String(30))
    passengers = Column(Integer)
    hyperdrive_rating = Column(String(10))
    crew = Column(Integer)
    length = Column(Integer)
    consumables = Column(String(20))
    starship_class = Column(String(100))
    manufacturer = Column(String(100))


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
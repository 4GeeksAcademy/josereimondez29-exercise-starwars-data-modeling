import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Country(Base):
    __tablename__ = 'country'
    ID = Column(Integer, primary_key=True)
    name = Column(String(10))

class User(Base):
    __tablename__ = 'user'
    ID = Column(Integer, primary_key=True)
    name = Column(String(20))
    pais = Column(Integer, ForeignKey('country.ID'))
    pais_relationship = relationship(Country)
    email = Column(String(50), unique=True)
    password = Column(String(25))

class Character(Base):
    __tablename__ = 'character'
    ID = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    height = Column(Integer)
    mass = Column(Integer)

class FavoriteCharacter(Base):
    __tablename__ = 'favorite_characters'
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.ID'))
    character_id = Column(Integer, ForeignKey('character.ID'))
    character_relationship = relationship(Character)

class Planets(Base):
    __tablename__ = 'planets'
    ID = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    
class FavoritePlanet(Base):
    __tablename__ = 'favorite_planets'
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.ID'))
    planet_id = Column(Integer, ForeignKey('planets.ID'))
    planet_relationship = relationship(Planets)   

class Vehicle_Starship(Base):
    __tablename__ = 'vehicle_starship'
    ID = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    
class FavoriteVehicleStarship(Base):
    __tablename__ = 'favorite_vehicles_starships'
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.ID'))
    vehicle_starship_id = Column(Integer, ForeignKey('vehicle_starship.ID'))
    vehicle_starship_relationship = relationship(Vehicle_Starship) 

class Movie(Base):
    __tablename__ = 'movies'
    ID = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    
class FavoriteMovie(Base):
    __tablename__ = 'favorite_movies'
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.ID'))
    movie_id = Column(Integer, ForeignKey('Movie.ID'))
    movie_relationship = relationship(Movie)     

    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

import os
import sys #provides a number of functions and variables that can be used to 
#manimpulate different parts of the Python run-tim environment
from sqlalchemy import Column, ForeignKey, Integer, String
#these come in handy when we're writing our mapper code
from sqlalchemy.ext.declarative import declarative_base
#declarative_base is used in the configuration and class code
from sqlalchemy.orm import relationship
#import relationship to creat our foreign key relationships.
from sqlalchemy import create_engine
#create_engine class is used in our configuration code at the end of the file.

Base = declarative_base() # make an instance of the declarative_base class 

class Restaurant(Base): #create a class to correspond with the two tables we want to create in our database.
    __tablename__ = 'restaurant' #variable that we will use to refer to our table
    name = Column(String(80), nullable = False) #mapper code creates variables that we will use to create columns within our database.
    id = Column(Integer, primary_key = True) #When we create a column, we must also pass an attribute to that column
#nullable = False means that if the name is not filled out we cannot create a new restaurant row in this database.
class MenuItem(Base):
    __tablename__ = 'menu_item'
    
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id')) # creates foreign key relationship between the restaurant class and menu class.
    restaurant = relationship(Restaurant)
#restaurant says look inside the restaurant table and retrieve the ID number whenever I ask for restaurant_id
#######insert at end of file #######

#Added Flask decorator method below
#This serializable function will help define what data we want to send across
#and put it in a format that Flask can easily use.
#Flask has a built-n package called JSONIFY that will allow us to easily configure
#an API endpoint for our application.
@property
def serialize(self):
    #Returns object data in easily serializeable format
    return {
        'name': self.name,
        'description': self.description,
        'id': self.id,
        'price': self.price,
        'course': self.course,
    }

engine = create_engine('sqlite:///restaurantmenu.db') 
#create an instance of our create_engine class and point to the database
#since we are using SQLite3 the engine will create a new file similar to MYSQL
Base.metadata.create_all(engine)
#goes into the database and adds the classes we will soon create as new tables
#in our data base

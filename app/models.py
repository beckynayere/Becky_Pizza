from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime





class Pizza:
    '''
    Pizza ito define Pizza objects
    '''

    __tablename__='pizza'
     
    id=db.Column(db.Integer,primary_key=True)
    size_price=db.Relationship ('Size',backref = 'size', lazy = 'dynamic ')

    flavor_price=db.Relationship('Flavor', backref = 'flavor', lazy = 'dynamic')
    toppings_price=db.Relationship('Toppings', backref = 'toppings', lazy ='dynamic')
    price=db.Column(db.Integer)
    



    def save_pizza(self):
        db.session.add(self)
        db.session.commit()
         

    

class Flavor(db.Model):
    __tablename__="flavor"

    id=db.Column(db.Integer,primary_key=True)
    pizza_id=db.Column(db.Integer)
    name=db.Column(db.String)
    price=db.Column(db.Integer)
    pizza = db.Column(db.Integer,db.ForeingKey("pizza.pizza_id"))
    

    def save_flavor (self):
        db.session.add(self)
        db.session.commit()


class Size (db.Model):

    __tablename__ = 'sizes'

    id = db.Column(db.Integer, primary_key = True)
    size = db.Column(db.String)
    price = db.Column(db.Integer)
    pizza = db.Column(db.Integer,db.ForeingKey("pizza.pizza_id"))
    


    def save_size(self):
        db.session.add(self)
        db.session.commit()


class Toppings(db.Model) :

    __tablename__ = 'toppings'

    id = db.Column(db.Integer, primary_key = True)
    toppings = db.Column(db.String)
    price =db.Column(db.Integer)
    pizza = db.Column(db.Integer,db.ForeingKey("pizza.pizza_id"))
    
    def save_toppings(self):
        db.session.add(self)
        db.session.commit()



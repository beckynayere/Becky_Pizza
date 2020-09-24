from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime





class Pizza:
    '''
    Pizza ito define Pizza objects
    '''

    __tablename__='pizza'
     
    id=db.Column(db.Integer,primary_key=True)
    size=db.Column(db.String)
    flavor=db.Column(db.String)
    toppings=db.Column(db.String)
    price=db.Column(db.Integer)

    all_pizza = []


    def __init__(self, id, toppings,flavor, price):

        self.id = id
        self.size= size
        self.flavor= flavor
        self.toppings=toppings
        self.price= price

    def save_pizza(self):
        Pizza.all_pizza.append(self)
        db.session.add(self)
        db.session.commit()
         

    @classsmethod
    def get_pizza(cls,pizza_id):
        """
        Returns a pizza depending on the id
        """
        pizza_size=Pizza.query.filter_by(id=pizza_id).all()
        return pizza_size

class Flavor(db.model):
    __tablename__="flavor"

    id=db.Column(db.Integer,primary_key=True)
    pizza_id=db.Column(db.Integer)
    pizza_size=db.Column(db.String)
    pizza_toppings=db.Column(db.String)
    pizza_price=db.relationship('Pizza',backref='pizza',lazy="dynamic")
    
    

    def save_flavor (self):
        db.session.add(self)
        db.session.commit()


    @classsmethod
    def get_flavor(cls,id) :
        flavor = Flavor.query.filter_by(flavor_id=id).all()
        return flavor
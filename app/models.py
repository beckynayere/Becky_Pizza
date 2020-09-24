from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime





class Pizza():
    __tablename__='pizza'
    
    id = db.Column(string (255)),primary_key = True)
    size=db.Column()



class Flavor():
     __tablename__ ='flavor'    
    

class Size():
    __tablename__ = 'size'

class Toppings():
    __tablename__ = 'toppings'
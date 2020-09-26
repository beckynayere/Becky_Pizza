from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,PasswordField,SubmitField
from wtforms.validators import Email,Required,EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):

    email = StringField("enter your email adress",validators = [Required(),Email()])
    password = PasswordField("enter password", validators = [Required()])
    remember = BooleanField("remember me")
    login = SubmitField("login ")

class Signup(FlaskForm):


    username = StringField("enter your username", validators=[Required()])
    email = StringField("enter your email", validators=[Required(),Email()])
    password = PasswordField("enter password" ,validators=[Required(),EqualTo("confirm_password", message= "password must be the same")])
    confirm_password = PasswordField ("confirm password", validators=[Required()])
    submit = SubmitField("signup")

    def validate_email(self,data_field):
        if User.query.filter_by(email=data_field.data):
            raise ValidationError("invalid email")
    
    def validate_username(self,data_field):
        if User.query.filter_by(username=data_field.data):
            raise ValidationError("username already taken")





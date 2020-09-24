from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class SignupForm(FlaskForm): 
    first_name = StringField("First Name", validators=[DataRequired("Please enter your First Name.")])    
    last_name = StringField("Last Name", validators=[DataRequired("Please enter your Last Name")])    
    email = StringField("Email", validators=[DataRequired("Please enter your email address."), Email("Pelase enter a valid email. name@host.com")])   
    password = PasswordField("Password", validators=[DataRequired("Please enter your password"), Length(min=6,message="Passwords must be at least 6 characters in length.")])   
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm): 

    email = StringField("Email", validators=[DataRequired("Please enter your email address.")])    
    password = PasswordField("Password", validators=[DataRequired("Please enter a password.")])   
    submit = SubmitField("Sign In")

class OrderForm(FlaskForm):    
    pizza = StringField("What type of pizza would you like?", validators=[DataRequired("Please enter a pizza.")])    
    time = FormField(TimeForm)    now_or_later = SelectField("Is your pizza for now or later?", choices=[("NOW", "Now"), ("LATER", "Later")])    delivery = SelectField("Would you like your pizza delivered or take out?",choices=[("DELIVERY", "Delivery"), ("TAKEOUT", "Take Out")])    submit = SubmitField("Place Order")






from flask_login import login_required,login_user,logout_user
from ..models import Pizza,Toppings,Flavor,Size,User
from flask import render_template,url_for,redirect,flash,request
from .forms import Signup,LoginForm
from .. import db,photos
from . import auth


@auth.route("/signup", methods=['POST','GET'])
def signup ():
    form = Signup() 
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data ,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for(".login"))


    return render_template("signup.html",form=form)

@auth.route("/login",methods=['POST','GET'] )
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by (email=form.email.data).first()
        if user.verify_password(form.password.data)and user is not None:
            login_user(user,form.remember.data)
            return redirect(url_for("main.index"))
        
        flash("invalid username or password")
    return render_template("login.html",form=form)

    

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("you have logged out")
    return redirect(url_for("main.index"))






from flask import render_template,url_for
from . import main
from ..models import Pizza,Toppings,Flavor,Size
from ..import db,photos
from flask_login import login_required


@main.route('/')
@login_required
def index ():
    return render_template('index.html')


@main.route('/uname/<name>')
def success(name):
    return 'welcome %s' % name

@main.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('uname', name = user))

    return render_template(login.html)


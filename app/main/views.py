from flask import render_template,request,redirect,url_for,abort, flash
from . import main
from flask_login import login_required, current_user
from ..models import Pizza, User
from .forms import PizzaForm
from flask.views import View,MethodView
from .. import db 

@main.route('/', methods = ['GET','POST'])
def index():

    '''
    Root page functions that return the home page and its data
    '''
    pizza = Pizza.query.filter_by().first()
    title = 'Welcome to Natty Nats Pizza House'
    extralarge = Pizza.query.filter_by(category="extralarge")
    largepizza = Pizza.query.filter_by(category = "largepizza")
    mediumpizza = Pizza.query.filter_by(category = "mediumpizza")
    smallpizza = Pizza.query.filter_by(category = "smallpizza")

    return render_template('index.html', title = title, pizza = pizza, extralarge=extralarge, largepizza= largepizza, mediumpizza = mediumpizza, smallpizza = smallpizza)
    
@main.route('/pizza/new/', methods = ['GET','POST'])
@login_required
def new_pizza():
    form = PizzaForm()

    if form.validate_on_submit():

        description = form.description.data
        title = form.title.data
        user = current_user
        category = form.category.data
        print(user.get_current_user().id)

        new_pizza = Pizza(user=current_user, title = title,description=description,category=category)
        db.session.add(new_pizza)
        db.session.commit()
        
        
        return redirect(url_for('.index'))
    return render_template('pizza.html',pizzaform=PizzaForm)

    

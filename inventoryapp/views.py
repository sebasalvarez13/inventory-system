from crypt import methods
from flask import Blueprint, render_template, request, flash
from .models import Product
from . import db

#Set up blueprint for Flask application
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/addproduct', methods = ['GET', 'POST'])
def addproduct():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        stock = request.form['stock']

        #Query database to check product does not already exist
        product = Product.query.filter_by(name = name).first() #returns first result
        if product:
            print('Prduct already exists in inventory')
        else:
            #Add new product
            new_product = Product(
                name = name,
                price = price,
                stock = stock
            )

            db.session.add(new_product)
            db.session.commit()

        print('product added')

    return render_template('add.html')


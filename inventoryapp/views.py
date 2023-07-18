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
        id = request.form['id']
        product_name = request.form['product_name']
        price = request.form['price']
        stock = request.form['stock']

        query = "UPDATE B_complete SET comment = %s, status = 'Used' WHERE device_name = %s"

        #Create sql connection
        #connection = engine.connect()

        #connection.execute(query, (new_comment, device))

        #Query database to check user does not exist previously
        product = Product.query.filter_by(product_name = product_name).first() #returns first result
        if product:
            print('Prduct already exists in inventory')
        else:
            #Add new product
            new_product = Product(
                id = id,
                product_name = product_name,
                price = price,
                stock = stock
            )

            db.session.add(new_product)
            db.session.commit()

        print('product added')

    return render_template('addproduct.html')


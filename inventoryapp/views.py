from flask import Blueprint, render_template, request
from .models import Products
from . import db
import pandas as pd

#Set up blueprint for Flask application
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')


@views.route('/availableproducts')
def availableproducts():
    #Open sql script to obtain Products join Vendors info
    path = "/mnt/c/users/sa55851/desktop/projects/scripts/inventory-system/inventoryapp/sql/products.sql"
    with open(path, 'r') as sql_script:
        query = sql_script.read()
    
    #Convert sql script result to a dataframe    
    products_df = pd.read_sql_query(query, con = db.engine)
   
    #Converts dataframe to html table    
    products_html = products_df.to_html(classes = "[table-responsive, table table-dark table-striped]", justify = 'left', index = False)

    return render_template('available.html', table = products_html)


@views.route('/addproduct', methods = ['GET', 'POST'])
def addproduct():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        stock = request.form['stock']

        #Query database to check product does not already exist
        product = Products.query.filter_by(name = name).first() #returns first result
        if product:
            print('Prduct already exists in inventory')
        else:
            #Add new product
            new_product = Products(
                name = name,
                price = price,
                stock = stock
            )

            db.session.add(new_product)
            db.session.commit()

        print('product added')

    return render_template('add.html')


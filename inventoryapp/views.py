from flask import Blueprint, render_template, request, flash
from .models import Products, Orders
from . import db
import pandas as pd
from datetime import datetime
from sqlalchemy import text
import random
import string

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
    #Select the name of vendors from Vendor table
    query = """SELECT id, name FROM vendors"""
    #Convert query result to dataframe. 
    vendors_df = pd.read_sql_query(query, con = db.engine)
    
    #Convert individual column to a list
    vendors_list = vendors_df.values.tolist()

    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        stock = request.form['stock']
        vendor_id = request.form['vendor']
 

        #Query database to check product does not already exist
        product = Products.query.filter_by(name = name).first() #returns first result
        if product:
            print('Prduct already exists in inventory')
        else:
            #Add new product
            new_product = Products(
                name = name,
                price = price,
                stock = stock,
                vendor_id = vendor_id
            )

            db.session.add(new_product)
            db.session.commit()

            print('product added')
    
    return render_template('add.html', value = vendors_list)


@views.route('/orders', methods = ['GET', 'POST'])
def addorder():
    #Select the name of vendors from Vendor table
    query = """SELECT id, name FROM vendors"""
    #Convert query result to dataframe. 
    vendors_df = pd.read_sql_query(query, con = db.engine)
    
    #Convert individual column to a list
    vendors_list = vendors_df.values.tolist()


    if request.method == 'POST':
        product_name = request.form['product_name']
        quantity = request.form['quantity']
        vendor_id = request.form['vendor']
        
        #Open sql script to obtain Products join Vendors info
        path = "/mnt/c/users/sa55851/desktop/projects/scripts/inventory-system/inventoryapp/sql/product_matches_vendor.sql"
        with open(path, 'r') as sql_script:
            query = sql_script.read()
        
        #Verify product and vendor match. If so, return count: 1
        result = db.session.execute(text(query), {'val1':product_name, 'val2' :vendor_id})
        #Returns query result as a dictionary enclosed in a LIST. 
        results_as_dict = result.mappings().all()

        print(results_as_dict)
        #If the return list is empty, it means that the vendor selected does not provide the requested product
        if not results_as_dict:
            flash('Vendor does not supply product selected', category = 'error')
        else:
            flash('Order placed successfully!')

            new_order = Orders(
                    product_name = product_name,
                    quantity = quantity,
                    vendor_id = vendor_id,
                    date = datetime.now(),
                    status = 'Ordered',
                    order_number  = generate_order_number()

            )

            db.session.add(new_order)
            db.session.commit()

    
    
    #Select query to display Orders table
    query = """SELECT * FROM orders"""
    #Convert sql script result to a dataframe    
    orders_df = pd.read_sql_query(query, con = db.engine)
    #Converts dataframe to html table    
    orders_html = orders_df.to_html(classes = "[table-responsive, table table-dark table-striped]", justify = 'center', index = False)

    return render_template('orders.html', value = vendors_list, table = orders_html)


def generate_order_number():
    #initializing size of string
    string_length = 10

    #using random.choices()
    #generating random strings
    #returns a list of characters. Use join to form a word
    order_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k = string_length))

    return(order_number)



    
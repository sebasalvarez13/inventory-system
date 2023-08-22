'''Define database models'''

from datetime import date
from telnetlib import STATUS
from . import db

class Products(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    stock = db.Column(db.Integer)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'))

class Vendors(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    country = db.Column(db.String(100))

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    product_name = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id')) 
    date = db.Column(db.DateTime)
    status = db.Column(db.String(100))
    order_number = db.Column(db.String(100), primary_key = True)

class Deliveries(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    vendor_id = db.Column(db.Integer) 
    date = db.Column(db.DateTime)
    employee_id = db.Column(db.Integer)
    order_number = db.Column(db.String(100), db.ForeignKey('orders.order_number'))
'''Define database models'''

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

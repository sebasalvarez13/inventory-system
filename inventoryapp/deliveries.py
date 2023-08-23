'''Handles the receiving of packages. Update deliveries table when an ords'''
from .models import Deliveries
from . import db
import pandas as pd
from datetime import datetime
from sqlalchemy import text

def scan_package(scan_order_number):
    #Scan new package. extract info from barcode data
    new_delivery = Deliveries(
        vendor_id = 1,
        date = datetime.now(),
        employee_id = 13,
        order_number = scan_order_number
    )

    db.session.add(new_delivery)
    db.session.commit()

def update_order_status(scan_order_number):
    path = "/mnt/c/users/sa55851/desktop/projects/scripts/inventory-system/inventoryapp/sql/update_order_status.sql"
    with open(path, 'r') as sql_script:
        query = sql_script.read()

    db.session.execute(text(query), {'val1': scan_order_number})
    db.session.commit()
    
    print('order updated')
    
def update_products_stock():
    path = "/mnt/c/users/sa55851/desktop/projects/scripts/inventory-system/inventoryapp/sql/update_products_stock.sql"
    with open(path, 'r') as sql_script:
        query = sql_script.read()

    db.session.execute(text(query))
    db.session.commit()
    
    print('product stock updated')
        

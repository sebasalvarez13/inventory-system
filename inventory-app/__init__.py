from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import pymysql


#Define database as an SQLAlchemy object
db = SQLAlchemy()
DB_NAME = 'inventory'

def create_app():
    app = Flask(__name__)

    #Define database location
    user = 'sebasalvarez13'
    password = 'BlueYeti27'
    host = 'localhost'
    port = '3306'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{host}:{port}/{DB_NAME}'
    
    #Initialize database
    db.init_app(app)

    return app


def create_database(app):
    #Check id db exists. If it does not exist, creates one
    if not path.exists('inventory' + DB_NAME):
        print('db does not exist')
        db.create_all(app = app)
    else:
        print('db exists')

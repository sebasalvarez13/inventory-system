from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import pymysql


#Create the SQLAlchemy extension. The db object gives you access to the db.Model class to define models, and the db.session to execute queries.
db = SQLAlchemy()
DB_NAME = 'inventory'

def create_app():
    #Create Flask app
    app = Flask(__name__)
    app.secret_key = 'asdfghjkl'

    #Define database information
    user = 'sebasalvarez13'
    password = 'BlueYeti27'
    host = 'localhost'
    port = '3306'

    #Configure the database, relative to the app instance folder
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{host}:{port}/{DB_NAME}'
    
    #Initialize the app with the extension. Basically tells the databse which app will be accesing it 
    db.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix = '/')


    return app



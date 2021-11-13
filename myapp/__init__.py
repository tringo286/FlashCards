import flask 
import os
from flask_sqlalchemy import SQLAlchemy


#gives current directory of this file
basedir = os.path.abspath(os.path.dirname(__file__))

#instance of Flask class
myapp_obj = flask.Flask(__name__)
myapp_obj.config.from_mapping(
	SECRET_KEY = 'it-dont-matter',
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
	SQLALCHEMY_TRACK_MODIFICATIONS = False)
	

db = SQLAlchemy(myapp_obj)

from myapp import routes, models

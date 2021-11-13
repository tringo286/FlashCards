from myapp import db
from datetime import datetime

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True)
	email = db.Column(db.String(128), unique=True)
	password  = db.Column(db.String(128))		


	def __repr__(self):
		return '<User {}>'.format(self.username)
		

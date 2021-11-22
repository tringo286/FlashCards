from myapp import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from myapp import login

class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True)
	email = db.Column(db.String(128), unique=True)
	password  = db.Column(db.String(128))
	todo = db.relationship('ToDo', backref='author', lazy='dynamic')
	
	def __init__(self, username, email):
		self.username = username
		self.email = email	

	def __repr__(self):
		return '<User {}>'.format(self.username)
		
	def set_password(self, password):
		self.password = generate_password_hash(password, method='sha256'
        )

	def check_password(self, password):
		return check_password_hash(self.password, password)
		
class ToDo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(256))
	timestamp = db.Column(db.DateTime, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
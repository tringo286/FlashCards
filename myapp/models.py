from myapp import db
from datetime import datetime

class User(db.Model):
	


	def __repr__(self):
		return '<City {}>'.format(self.city_name)
		

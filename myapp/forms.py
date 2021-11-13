from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	city_name =  StringField('Username', validators=[DataRequired()])
	city_rank = PasswordField('password')	
	remember_me = BooleanField('Remember Me', default=False)
	submit = SubmitField("Submit")

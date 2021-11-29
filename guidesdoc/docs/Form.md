class LoginForm(FlaskForm):
	
        """

	"""
        __tablename__ = 'users'
        username = StringField('Username', validators=[DataRequired()])
        password = PasswordField('Password', validators=[DataRequired()])
        remember_me = BooleanField('Remember Me', default=False)
        submit = SubmitField('Log In')

class SignupForm(FlaskForm):

        """

	"""
        username = StringField('Username', validators=[DataRequired()])
        email = StringField('Email', validators=[DataRequired()])
        password = PasswordField('Password', validators=[DataRequired(), Length(min=6, message='Select a stronger password.')])
        confirm = PasswordField('Confirm Your Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match.')])
        submit = SubmitField('Register')

class ToDoForm(FlaskForm):
       
	"""

	"""
        body = StringField('To Do Item', validators=[DataRequired()])
        status = SelectField('Status', choices = ['Todo', 'In Progress', 'Complete'])
        submit = SubmitField('Submit')

class SearchForm(FlaskForm):
       
	"""

	"""
	result = StringField('Result', validators=[DataRequired()])
	submit = SubmitField('Search')

class RenameForm(FlaskForm):

	"""

	"""			
	file = FileField('File', validators=[FileRequired()])
	new_name = StringField('New name', validators=[DataRequired()])	
	submit = SubmitField('Rename')

class MdToPdfForm(FlaskForm):

	"""

	"""
	file = FileField('File', validators=[FileRequired()])	
	submit = SubmitField('Convert')





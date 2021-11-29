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
	This class creates a search form for the find-text-in-files feature

            Parameters:
                    result (StringField): A single line of text
                    sumbit (SubmitField): A submit button 
            Returns:
                    Show a search form for the find-text-in-files feature
	"""
	result = StringField('Result', validators=[DataRequired()])
	submit = SubmitField('Search')

class RenameForm(FlaskForm):

	"""
	This class creates a rename form for the rename-file feature

            Parameters:
                    file (FileField): A file
		    new_name(StringField): A single line of text
                    sumbit (SubmitField): A submit button 
            Returns:
                    Show a rename form for the rename-file feature
	"""			
	file = FileField('File', validators=[FileRequired()])
	new_name = StringField('New name', validators=[DataRequired()])	
	submit = SubmitField('Rename')

class MdToPdfForm(FlaskForm):

	"""
	This class creates a markdown-to-pdf form for the markdown-to-pdf feature

            Parameters:
                    file (FileField): A file		    
                    sumbit (SubmitField): A submit button 
            Returns:
                    Show a markdown-to-pdf form for the markdown-to-pdf feature
	"""
	file = FileField('File', validators=[FileRequired()])	
	submit = SubmitField('Convert')





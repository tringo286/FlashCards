from myapp import myapp_obj
from myapp.forms import LoginForm, SignupForm
from flask import render_template, request, flash, redirect
from myapp.models import User
from myapp import db
from sqlalchemy import desc

@myapp_obj.route("/login", methods=['GET','POST'])
def login():
	form = LoginForm()	
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user and user.check_password(password=form.password.data):
			return redirect("/home")
		flash('Invalid username/password combination')
	return render_template('login.html', form=form)

@myapp_obj.route("/signup", methods=['GET','POST'])
def signup():
	form = SignupForm()
	if form.validate_on_submit():
		flash(f'Welcome!')
		username = form.username.data
		email = form.email.data
		password = form.password.data
		user = User(username, email)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		return redirect("/login")
	return render_template('signup.html', form=form)

@myapp_obj.route("/home", methods=['GET','POST'])
def home():
        return render_template('home.html')
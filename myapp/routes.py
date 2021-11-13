from myapp import myapp_obj
from myapp.forms import LoginForm
from flask import render_template, request, flash, redirect
from myapp.models import User
from myapp import db
from sqlalchemy import desc

@myapp_obj.route("/", methods=['GET','POST'])
def home():
	
	return render_template('home.html')

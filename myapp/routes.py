from sqlalchemy.sql.expression import delete
from myapp import myapp_obj
import myapp
from myapp.forms import LoginForm, SignupForm, ToDoForm, SearchForm, RenameForm, MdToPdfForm 
from flask import render_template, request, flash, redirect, make_response, url_for
from myapp.models import User, ToDo, load_user, Flashcard
from myapp.render import Render
from myapp import db
import markdown
from sqlalchemy import desc, update, delete, values
from flask_login import current_user, login_user, logout_user, login_required
import pdfkit
from werkzeug.utils import secure_filename
import os, sys
from markdown import markdown
ALLOWED_EXTENSIONS = {'md'}
UPLOAD_FOLDER = 'myapp/upload/'
myapp_obj.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = 'myapp/text/'

@myapp_obj.route("/")
def welcome():
	return render_template("welcome.html")

@myapp_obj.route("/loggedin")
@login_required
def log():
    return 'Hi you are logged in'

@myapp_obj.route("/logout")
def logout():
    logout_user()
    return redirect('/')

@myapp_obj.route("/login", methods=['GET','POST'])
def login():
	form = LoginForm()	
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Login invalid username or password!')
			return redirect('/login')
		login_user(user, remember=form.remember_me.data)
		#flash(f'Login requested for user {form.username.data},remember_me={form.remember_me.data}')
		#flash(f'Login password {form.password.data}')
		return redirect('/home')
	return render_template('login.html', form=form)
	
@myapp_obj.route("/members/<string:name>/")
def getMember(name):
	return 'Hi ' + name

@myapp_obj.route("/members/delete")
def deleteMember():
	user = current_user.id
	db.session.query(User).filter(User.id == user).delete(synchronize_session=False)
	db.session.commit()
	return login()
	
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

@myapp_obj.route("/todo", methods=['GET', 'POST'])
def todo():
	title = 'To Do List'
	form=ToDoForm()
	if form.validate_on_submit():
		item = form.body.data
		status = form.status.data
		user_id = current_user.id
		todo = ToDo(item, user_id, status)
		db.session.add(todo)
		db.session.commit()	
	list = ToDo.query.filter(ToDo.user_id).order_by(ToDo.status.desc())
	return render_template('todo.html', title=title, form=form, list=list)

@myapp_obj.route("/todo/inprog/<string:item>", methods=['GET', 'POST'])
def inProgress(item):
	task = item
	user_id = current_user.id
	update = "In Progress"
	db.session.query(ToDo).filter(ToDo.body == task).update({ToDo.status : update })
	db.session.commit()
	return redirect("/todo")

@myapp_obj.route("/todo/<string:item>", methods=['GET', 'POST'])
def editTodo(item):
	task = item
	user_id = current_user.id
	update = "Todo"
	db.session.query(ToDo).filter(ToDo.body == task).update({ToDo.status : update })
	db.session.commit()
	return redirect("/todo")

@myapp_obj.route("/todo/comp/<string:item>", methods=['GET', 'POST'])
def complete(item):
	task = item
	user_id = current_user.id
	update = "Complete"
	db.session.query(ToDo).filter(ToDo.body == task).update({ToDo.status : update })
	db.session.commit()
	return redirect("/todo")

@myapp_obj.route("/todo/delete/<string:item>", methods=['GET', 'POST'])
def deleteTodo(item):
	task = item
	user_id = current_user.id
	update = "Complete"
	db.session.query(ToDo).filter(ToDo.body == task, ToDo.user_id == user_id).delete(synchronize_session=False)
	db.session.commit()
	return redirect("/todo")

@myapp_obj.route("/render")
def render():
	return Render.render('myapp/test.md')

@myapp_obj.route("/search", methods=['GET', 'POST'])
def search():	
	form = SearchForm()		
	if form.validate_on_submit():
		result = form.result.data
		results = []
		files = os.listdir(basedir)		
		for file in files:
			text = os.path.join(f"{basedir}/{file}")		
			with open (text, 'r') as f:
				if result in f.read():
					results.append(f"{file}")			
		return render_template("search.html", form=form, results=results)
	return render_template("search.html", form=form)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@myapp_obj.route('/markdown-to-pdf', methods=['GET', 'POST'])
def mdToPdf():    
    form = MdToPdfForm();
    if request.method == 'POST':  
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)           
            file.save(os.path.join(myapp_obj.config['UPLOAD_FOLDER'], filename))
            input_file = 'myapp/upload/' + filename            
            output_file = input_file.split(".md")
            output_file = output_file[0] + '.pdf'
            with open(input_file, 'r') as f:
            	html = markdown(f.read(), output_format='html4')
            pdf = pdfkit.from_string(html, False)
            response = make_response (pdf)
            response.headers["Content-Type"] = "application/pdf"
            response.headers["Content-Disposition"] = "inline; filename = output.pdf"
            return response          
    return render_template("md_to_pdf.html", form=form)

@myapp_obj.route('/rename', methods=['GET', 'POST'])
def upload_file():
    form = RenameForm()
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(myapp_obj.config['UPLOAD_FOLDER'], filename))  
            new_name = request.form['new_name']           
            os.rename(UPLOAD_FOLDER + filename, UPLOAD_FOLDER + new_name + '.md')	   
            flash(f'Your file was successfully renamed by {form.new_name.data}.md and stored in myapp/upload/') 
    return render_template("rename.html", form=form)


    


from sqlalchemy.sql.expression import delete
from myapp import myapp_obj
from datetime import date
import myapp

from myapp.forms import LoginForm, SignupForm, ToDoForm, SearchForm, RenameForm 
from flask import render_template, request, flash, redirect, make_response, url_for
from myapp.models import User, ToDo, load_user, Flashcard, FlashCard, Activity

from myapp.render import Render
from myapp import db
import markdown
from sqlalchemy import desc, update, delete, values
from flask_login import current_user, login_user, logout_user, login_required
import pdfkit
from werkzeug.utils import secure_filename
import os
from markdown import markdown
ALLOWED_EXTENSIONS = {'md'}
UPLOAD_FOLDER = 'myapp/upload'
myapp_obj.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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


@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()	
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Login invalid username or password!')
			return redirect('/login')
		login_user(user, remember=form.remember_me.data)		
		return redirect('/home')
	return render_template('login.html', form=form)
	
@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return 'Hi ' + name

@myapp_obj.route("/members/delete")
def deleteMember():
    user = current_user.id
    db.session.query(User).filter(
        User.id == user).delete(synchronize_session=False)
    db.session.commit()
    return login()


@myapp_obj.route("/signup", methods=['GET', 'POST'])
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

@myapp_obj.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@myapp_obj.route("/todo", methods=['GET', 'POST'])
def todo():
    title = 'To Do List'
    form = ToDoForm()
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
    db.session.query(ToDo).filter(
        ToDo.body == task).update({ToDo.status: update})
    db.session.commit()
    return redirect("/todo")


@myapp_obj.route("/todo/<string:item>", methods=['GET', 'POST'])
def editTodo(item):
    task = item
    user_id = current_user.id
    update = "Todo"
    db.session.query(ToDo).filter(
        ToDo.body == task).update({ToDo.status: update})
    db.session.commit()
    return redirect("/todo")


@myapp_obj.route("/todo/comp/<string:item>", methods=['GET', 'POST'])
def complete(item):
    task = item
    user_id = current_user.id
    update = "Complete"
    db.session.query(ToDo).filter(
        ToDo.body == task).update({ToDo.status: update})
    db.session.commit()
    return redirect("/todo")


@myapp_obj.route("/todo/delete/<string:item>", methods=['GET', 'POST'])
def deleteTodo(item):
    task = item
    user_id = current_user.id
    update = "Complete"
    db.session.query(ToDo).filter(ToDo.body == task,
                                  ToDo.user_id == user_id).delete(synchronize_session=False)
    db.session.commit()
    return redirect("/todo")


@myapp_obj.route("/render")
def render():
    return Render.render('myapp/test.md')


@myapp_obj.route("/search", methods=['GET', 'POST'])
def search():	
	search = SearchForm()		
	if search.validate_on_submit():
		result = Flashcard.query.filter_by(title = search.result.data).first()
		if not result or result is None:	
			flash('No results found!')			
			return redirect('/search')
		flash(f'Result: {search.result.data}') 
		return redirect('/search')
	return render_template("search.html", form=search)

@myapp_obj.route("/rename", methods=['GET', 'POST'])
def rename():	
	rename = RenameForm()	
	if rename.validate_on_submit():
		result = Flashcard.query.filter_by(title = rename.old_name.data).first()
		if not result or result is None:	
			flash('No flashcard found!')			
			return redirect('/rename')		 
		Flashcard.title = request.form['new_name']
		db.session.commit()
		flash(f'{rename.old_name.data} was renamed by {rename.new_name.data}') 
		return redirect('/rename')
	return render_template("rename.html", form=rename)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@myapp_obj.route('/markdown-to-pdf', methods=['GET', 'POST'])
def mdToPdf():    
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
    return render_template("md_to_pdf.html")
  
@myapp_obj.route("/index")
def index():
    title_homepage = 'Top Page'
    greeting = "Quan"
    return render_template("index.html", title_pass=title_homepage, XX=greeting)

@myapp_obj.route("/visualizehours", methods=["POST", "GET"])
def visualize():
    title_homepage = 'Top Page'
    categories = ['Math', 'Physics', 'English', 'Computer']

    u1 = User(username='morning', email='m@gmail.com')
    db.session.add(u1)
    db.session.commit()
    u2 = User(username='evening', email='n@gmail.com')
    db.session.add(u2)
    db.session.commit()

    u1 = User.query.filter_by(username=u1.username).first()
    u2 = User.query.filter_by(username=u2.username).first()

    if u1 is not None:
        today = date.today()
        a = Activity(timeamount=135, owner=u1)
        db.session.add(a)
        db.session.commit()
        b = Activity(timeamount=100, owner=u1)
        db.session.add(b)
        db.session.commit()
        b1 = Activity(timeamount=300, owner=u1)
        db.session.add(b1)
        db.session.commit()
        b2 = Activity(timeamount=250, owner=u1)
        db.session.add(b2)
        db.session.commit()
        b3 = Activity(timeamount=600, owner=u1)
        db.session.add(b3)
        db.session.commit()
        c = Activity(timeamount=88, owner=u2)
        db.session.add(c)
        db.session.commit()

        z = FlashCard(title='zzzzzzz', defination='00000000',
                      category='Math', owner=u1)
        db.session.add(z)
        db.session.commit()
        z1 = FlashCard(title='zzzzz', defination='11111111',
                       category=categories[0], owner=u1)
        db.session.add(z1)
        db.session.commit()
        z2 = FlashCard(title='zzzzz', defination='222222',
                       category=categories[0], owner=u1)
        db.session.add(z2)
        db.session.commit()
        z3 = FlashCard(title='zzzzzz', defination='33333',
                       category=categories[1], owner=u1)
        db.session.add(z3)
        db.session.commit()
        z4 = FlashCard(title='zzzzzz', defination='444444',
                       category=categories[2], owner=u1)
        db.session.add(z4)
        db.session.commit()
        x = FlashCard(title='xxxxx', defination='00000',
                      category=categories[0], owner=u2)
        db.session.add(x)
        db.session.commit()

        data_flashcard = db.session.query(db.func.sum(FlashCard.count_category), FlashCard.category).group_by(
            FlashCard.category).order_by(FlashCard.category).filter(FlashCard.owner_id == u1.id).all()

        data_acitivity = db.session.query(Activity.timeamount, Activity.usertime).group_by(
            Activity.usertime).order_by(Activity.usertime).filter(Activity.owner_id == u1.id).all()

    print(f'data: {data_flashcard}')

    category_labels = []
    count_category_labels = []
    for count_ctr, ctr in data_flashcard:
        category_labels.append(ctr)
        count_category_labels.append(count_ctr)

    amount_labels = []
    date_labels = []
    for amounts, dates in data_acitivity:
        date_labels.append(dates.strftime("%m-%d-%y"))
        amount_labels.append(amounts)

    return render_template("visualizehours.html", amounts=amount_labels, dates=date_labels,
                           category=category_labels, c_category=count_category_labels)
    



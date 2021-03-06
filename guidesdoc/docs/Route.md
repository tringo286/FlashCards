@myapp_obj.route("/")
def welcome():

    """
    This function returns the welcome.html page

    Parameters:
    ----------
        none
    Return:
    ------
        redirect user to welcome page
    """

    return render_template("welcome.html")


@myapp_obj.route("/loggedin")
@login_required
def log():
    
    """
    This function returns 'Hi you are logged in'

    Parameters:
    ----------
        none
    Return:
    ------
        "Hi you are logged in"
    """

    return 'Hi you are logged in'


@myapp_obj.route("/logout")
def logout():
    
    """
    This function logs out the user

    Parameters:
    ----------
        none
    Return:
    ------
        redirects to '/'
    """

    logout_user()
    return redirect('/')


@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():

    """
    This function returns the login page with the LoginForm

    Parameters:
    ----------
        none
    Return:
    ------
        on successful login redirects to 'home.html'
    """

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Login invalid username or password!')
            return redirect('/login')
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('home', username=user))
    return render_template('login.html', form=form)


@myapp_obj.route("/members/<string:name>/")
def getMember(name):

    """
    This function returns the user's name

    Parameters:
    ----------
        none
    Return:
    ------
        Hi + user's name
    """

    return 'Hi ' + name


@myapp_obj.route("/members/delete")
def deleteMember():

    """
    This function deletes a user from the database

    Parameters:
    ----------
        none
    Return:
    ------
        redirects to login page
    """

    user = current_user.id
    db.session.query(User).filter(
        User.id == user).delete(synchronize_session=False)
    db.session.commit()
    return login()


@myapp_obj.route("/signup", methods=['GET', 'POST'])
def signup():

    """
    This function returns the signup page with the SignUpForm

    Parameters:
    ----------
        none
    Return:
    ------
        redirects to login.html
    """

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


@myapp_obj.route("/home/<string:username>", methods=['GET', 'POST'])
def home(username):

    """
    This function goes to user's home page

    Parameters:
    ----------
        none
    Return:
    ------
        redirects to user's homepage
    """

    return render_template('home.html', username=username)


@myapp_obj.route("/todo", methods=['GET', 'POST'])
def todo():

    """
    This function returns the ToDo list page with the ToDoForm

    Parameters:
    ----------
        none
    Return:
    ------
        redirect to todo.html
    """

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

    """
    This function changes the todo list item to status: In Progress

    Parameters:
    ----------
        item (string): todo list item's body
    Return:
    ------
        redirect to todo.html
    """

    task = item
    user_id = current_user.id
    update = "In Progress"
    db.session.query(ToDo).filter(
        ToDo.body == task).update({ToDo.status: update})
    db.session.commit()
    return redirect("/todo")


@myapp_obj.route("/todo/<string:item>", methods=['GET', 'POST'])
def editTodo(item):

    """
    This function changes the todo list item to status: Todo

    Parameters:
    ----------
        item (string): todo list item's body
    Return:
    ------
        redirect to todo.html
    """

    task = item
    user_id = current_user.id
    update = "Todo"
    db.session.query(ToDo).filter(
        ToDo.body == task).update({ToDo.status: update})
    db.session.commit()
    return redirect("/todo")


@myapp_obj.route("/todo/comp/<string:item>", methods=['GET', 'POST'])
def complete(item):

    """
    This function changes the todo list item to status: Complete

    Parameters:
    ----------
        item (string): todo list item's body
    Return:
    ------
        redirect to todo.html
    """
    task = item
    user_id = current_user.id
    update = "Complete"
    db.session.query(ToDo).filter(
        ToDo.body == task).update({ToDo.status: update})
    db.session.commit()
    return redirect("/todo")


@myapp_obj.route("/todo/delete/<string:item>", methods=['GET', 'POST'])
def deleteTodo(item):

    """
    This function deletes a task from the ToDo list

    Parameters:
    ----------
        item (string): todo list item's body
    Return:
    ------
        redirect to todo.html
    """

    task = item
    user_id = current_user.id
    update = "Complete"
    db.session.query(ToDo).filter(ToDo.body == task,
                                  ToDo.user_id == user_id).delete(synchronize_session=False)
    db.session.commit()
    return redirect("/todo")


@myapp_obj.route("/render")
def rendering():

    """
    This function lists the user's uploaded files

    Parameters:
    ----------
        none
    Return:
    ------
        return 'render.html'
    """

    basedir = 'myapp/upload/'
    files = os.listdir(basedir)
    return render_template('render.html', files=files)

@myapp_obj.route("/render/<string:file>")
def renderer(file):

    """
    This function renders the choosen file into html to be displayed

    Parameters:
    ----------
        file (string): the choosen filename
    Return:
    ------
        returns the .md file rendered into html
    """

    file_path = "myapp/upload/" + file
    html = Render.render(file_path)
    return html

@myapp_obj.route("/search", methods=['GET', 'POST'])
def search():

    """
    This function creates a route for the find-text-in-files feature

            Parameters:
                    text: get form the input box                   
            Returns:
                    Show a page for the find-text-in-files feature
    """
    
    form = SearchForm()
    if form.validate_on_submit():
        result = form.result.data
        results = []
        files = os.listdir(basedir)
        for file in files:
            text = os.path.join(f"{basedir}/{file}")
            with open(text, 'r') as f:
                if result in f.read():
                    results.append(f"{file}")
        return render_template("search.html", form=form, results=results)
    return render_template("search.html", form=form)


def allowed_file(filename):

    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@myapp_obj.route('/markdown-to-pdf', methods=['GET', 'POST'])
def mdToPdf():
    """
    This function creates a route for the markdown-to-pdf feature

            Parameters:
                    file: browse from user's directory                    
            Returns:
                    Show a page for the markdown-to-pdf feature
    """
    form = MdToPdfForm()
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
            file.save(os.path.join(
                myapp_obj.config['UPLOAD_FOLDER'], filename))
            input_file = 'myapp/upload/' + filename
            output_file = input_file.split(".md")
            output_file = output_file[0] + '.pdf'
            with open(input_file, 'r') as f:
                html = markdown(f.read(), output_format='html4')
            pdf = pdfkit.from_string(html, False)
            response = make_response(pdf)
            response.headers["Content-Type"] = "application/pdf"
            response.headers["Content-Disposition"] = "inline; filename = output.pdf"
            return response
    return render_template("md_to_pdf.html", form=form)


@myapp_obj.route('/rename', methods=['GET', 'POST'])
def upload_file():
    """
    This function creates a route for the rename-file feature

            Parameters:
                    file: browse from user's directory 
                    new_name: get from input box
            Returns:
                    Show a page for the rename-file feature
    """
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
            file.save(os.path.join(
                myapp_obj.config['UPLOAD_FOLDER'], filename))
            new_name = request.form['new_name']
            os.rename(UPLOAD_FOLDER + filename,
                      UPLOAD_FOLDER + new_name + '.md')
            flash(
                f'Your file was successfully renamed by {form.new_name.data}.md and stored in myapp/upload/')
    return render_template("rename.html", form=form)


@myapp_obj.route("/index/<string:user_name>", methods=["POST", "GET"])
def index(user_name):

    title_homepage = 'Top Page'
    greeting = user_name
    return render_template("index.html", title_pass=title_homepage, XX=greeting)


@myapp_obj.route("/visualizehours", methods=["POST", "GET"])
def visualize():

    """
    This class represent for handling visualize hours feature
    
    Parameters:
    ----------
        username: get from homepage
        activity: filter by username
        flashcard: filter by username
    Return:
    ------
        Perform a page with charts
    """

    title_homepage = 'Top Page'
    categories = ['Math', 'Physics', 'English', 'Computer']
    exists = db.session.query(User.id).filter_by(
        username='morning').first() is not None

    if not exists:
        user1 = User(username='morning',
                     email='m@gmail.com')
        db.session.add(user1)
        db.session.commit()
        user2 = User(username='evening',
                     email='e@gmail.com')
        db.session.add(user2)
        db.session.commit()

    u1 = User.query.filter_by(username='morning').first()
    u2 = User.query.filter_by(username='evening').first()

    if u1 is not None:
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


@myapp_obj.route("/trackhours", methods=["POST", "GET"])
def trackinghours():

    """
    This class represent for handling tracking hours feature
    
    Parameters:
    ----------
        username: get from homepage
        flashcard: filter by username
    Return:
    ------
        Perform a page with tables that show their activities
    """
    u1 = User.query.filter_by(username='morning').first()
    data_flashcard = db.session.query(FlashCard.id, FlashCard.times_created, FlashCard.title, FlashCard.category).order_by(
        FlashCard.times_created.desc()).filter(FlashCard.owner_id == u1.id).all()

    date_labels = []
    for _, dates, _, _ in data_flashcard:
        temp_date = dates.strftime("%m-%d-%Y")
        if temp_date not in date_labels:
            date_labels.append(temp_date)
    print(date_labels)
    return render_template("trackhours.html", entries=data_flashcard, current_dates=date_labels[0], list_dates=date_labels)


@myapp_obj.route('/delete-post/<int:entry_id>')
def delete(entry_id):

    """
    This class represent for handling delete from table in tracking hour feature
    
    Parameters:
    ----------
        entry_id: int
    Return:
    ------
        redirect user to tracking hours page
    """
    entry = FlashCard.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for("trackinghours"))

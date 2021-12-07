from myapp import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from myapp import login


class User(UserMixin, db.Model):
    """
        This class represent for User table in database

        Attributes:
        ----------
        id: int (primary key)
        username: string
        email: string
        password: string
        to_do: object (foreign key)
        activities: Object (foreign key)
        flaskcard: Object (foreign key)

        Function:
        ---------
        __init__: constructor with 2 parameter username, email
        __repr__: representation a output
        set_password: auto generate password
        check_password: get and check password
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    to_do = db.relationship('ToDo', backref='user', lazy='dynamic')
    activities = db.relationship('Activity', backref="owner", lazy='dynamic')
    flaskcards = db.relationship('FlashCard', backref='owner', lazy='dynamic')
    card = db.relationship('Cards', backref='user', lazy='dynamic')

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return f'{self.username}'

    def set_time_login(self, timelogin):
        self.timelogin = timelogin

    def set_time_logout(self, timeloguot):
        self.timelogin = timeloguot

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Flashcard(db.Model):
    """
This class represent for FlashCard table in database

Attributes:
----------
id: int (primary key)
title: string
defination: string
category: string
count_catergory: int
times_created: datetime
owner_id: Object (foreign key)
"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True, index=True)
    body = db.Column(db.String(256))

    def __init__(self, title, body):
        self.title = title
        self.body = body

    def __repr__(self):
        return f'<Flashcard {self.id}: {self.title}>'


class ToDo(db.Model):
    """
This class represents a ToDo list item in the database

Attributes:
----------
id: int (primary key)
body: string 
status: string
timestamp: DateTime
user_id: Integer (foreign key)


Function:
---------
__init__: constructor with 3 parameter body, user_id, and status 
    """
    __tablename__ = 'todo_list'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256))
    status = db.Column(db.String(30))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, body, user_id, status):
        self.body = body
        self.user_id = user_id
        self.status = status


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Activity(db.Model):
    """
    This class represent for Activity table in database

    Attributes:
    ----------
    id: int (primary key)
    timeamount: int
    usertime: datetime
    owner_id: Object (foreign key)
    """
    __tablename__ = 'user_activity'
    id = db.Column(db.Integer, primary_key=True)
    timeamount = db.Column(db.Integer, nullable=False)
    usertime = db.Column(db.DateTime, default=datetime.utcnow)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class FlashCard(db.Model):
    """
        This class represent for FlashCard table in database

        Attributes:
        ----------
        id: int (primary key)
        title: string
        defination: string
        category: string
        count_catergory: int
        times_created: datetime
        owner_id: Object (foreign key)
        """
    __tablename__ = 'user_flaskcard'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    defination = db.Column(db.String(128))
    category = db.Column(db.String(16))
    count_category = db.Column(db.Integer, nullable=False, default=1)
    times_created = db.Column(db.DateTime, default=datetime.utcnow)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Cards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(64))
    answer = db.Column(db.String(64))
    order = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Cards {self.question}>'


class Notes(db.Model):
	__tablename__ = 'notes'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))
	body = db.Column(db.String(2000))
	tag = db.Column(db.String(30))
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __init__(self, name, user_id, body):
		self.name = name
		self.user_id = user_id
		self.body = body

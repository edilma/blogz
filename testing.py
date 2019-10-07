from flask import Flask, request, redirect, render_template, flash, session
from flask_sqlalchemy import SQLAlchemy
from helpers import *

app = Flask(__name__)
app.config['DEBUG'] = True
#TODO fix the database conexion
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blogz:edilma@localhost:8889/blogz'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'Lily'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique = True, nullable=False)
    password = db.Column(db.String(30))
    posts = db.relationship('Post', backref='owner')

    def __init__(self,username,password):
        self.username = username
        self.password= password


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    content = db.Column(db.Text)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self,title,content, owner):
        self.title = title
        self.content= content
        self.owner= owner








@app.route('/', methods=['POST', 'GET'])
def index():
    user = User.query.filter_by(username=username).all()
    print (user)
    return render_template('index.html',user=user)


        



@app.route('/login', methods=['GET'])
def display():
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            session['username'] = username
            flash("Logged in")
            return redirect('/')
        else:
            flash('User password incorrect, or user does not exist', 'error')
    return render_template('login.html')



@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            session['username'] = username
            flash("Logged in")
            return redirect('/')
        else:
            flash('User password incorrect, or user does not exist', 'error')
    return render_template('login.html')










if __name__ == "__main__":
    app.run()
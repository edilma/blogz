from flask import Flask, request, redirect, render_template, flash, session, url_for
from flask_sqlalchemy import SQLAlchemy
from helpers import *

app = Flask(__name__)
app.config['DEBUG'] = True
#TODO fix the database conexion
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blogz:edilma@localhost:8889/blogz'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'Lily'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    content = db.Column(db.Text)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self,title,content, owner):
        self.title = title
        self.content= content
        self.owner= owner

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique = True, nullable=False)
    password = db.Column(db.String(30))
    posts = db.relationship('Post', backref='owner')

    def __init__(self,username,password):
        self.username = username
        self.password= password
        self.owner_id= owner_id




@app.route('/', methods=["GET"])
def index():
    return render_template ('signup.html')







if __name__ == "__main__":
    app.run()
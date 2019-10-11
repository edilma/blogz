from app import db
from hashutils import *

#Class of user.  A user can have many posts
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique = True, nullable=False)
    hash = db.Column(db.String(250))
    posts = db.relationship('Post', backref='owner')

    def __init__(self,username,password):
        self.username = username
        self.pasword_hash = make_pw_hash(password)
        

    def __repr__(self):
        return '<User %r>' % self.email

#Class of Post.  A post is relate to only one user
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    content = db.Column(db.Text)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self,title,content, owner):
        self.title = title
        self.content= content
        self.owner= owner
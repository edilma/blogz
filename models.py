from app import db
from hashutils import make_pw_hash

#Class of user.  A user can have many posts
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique = True, nullable=False)
    pw_hash = db.Column(db.String(30))
    posts = db.relationship('Post', backref='owner')

    def __init__(self,username,password):
        self.username = username
        self.pw_hash= make_pw_hash(password)

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
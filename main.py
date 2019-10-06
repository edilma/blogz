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



@app.route('/', methods=["GET"])
def index():
    return render_template ('signup.html')







@app.route('/signup', methods=['POST'])
def register():  
    
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    infoUser =[username,password,verify]
    errors = validateUserinfo(infoUser)
    #print (errors)
    if (errors[0] !='') or  (errors[1] !='') or  (errors[2] !='')  :
        return render_template('signup.html',errors=errors, infoUser=infoUser)
    else:
        return "thanks"

        


    # TODO - validate user's data

    # existing_user = User.query.filter_by(email=email).first()
    # if not existing_user:
    #     new_user = User(email, password)
    #     db.session.add(new_user)
    #     db.session.commit()
    #     session['email'] = email
    #     return redirect('/')
    # else:
    #     flash("The email <strong>{0}</strong> is already registered".format(email), 'danger')

    # return render_template('register.html')




@app.route('/newpost', methods=["GET"])
def create():
    #posts = Post.query.all()
    #return render_template('posts.html', title=title, content=content)
    return render_template('newpost.html')


@app.route('/blog', methods=["GET"])
def viewPosts():
    id =  request.args.get('id')
    if id:
        posts = Post.query.filter_by(id=id).all()
    else:
        posts = Post.query.all()

    return render_template('/posts.html',posts=posts)



@app.route('/', methods=['POST'])
def GetContent():
    title= request.form ['title']
    content = request.form ['content']
    #error = None
    if not title:
        flash ("Title can NOT be empty")
        error="error"
        return render_template('write.html', content=content)
    if not content:
        flash ("Content can NOT be empty")
    #   error='error'
        return render_template('write.html',title=title)
        
    #what to do if there is an error
    else:
        new_post = Post(title,content)
        db.session.add(new_post)
        db.session.commit()
        #posts = Post.query.all()
        #post_id = new_post.id 
        posts = Post.query.filter_by(id=new_post.id).first()
        
        return render_template('blog_post.html',posts=posts)
        
        

    
    
    





if __name__ == "__main__":
    app.run()
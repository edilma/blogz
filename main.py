from flask import  request, redirect, render_template, flash, session, url_for
from models import User, Post
from app import app, db
from helpers import *
from hashutils import *


@app.before_request
def require_login():
    allowed_routes = ['login', 'viewPosts','register','index']
    if request.endpoint not in allowed_routes and 'username' not in session:
        return redirect('/login')


#route login - when a user tries to log in: allow and send to new post or errors flashed, click in signup
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_pw_hash(password,user.pw_hash):
            session['username'] = user.username
            flash("Logged in")
            return redirect('/newpost', session['username'])
        else:
            return redirect ('/signup')
            
        

        
#Route signgup.  Request the user information and verify it using the verify
#function that is located in the helpers.py file. 
@app.route('/signup', methods=['POST', 'GET'])
def register():
    if request.method =='GET':
        return render_template('signup.html' ,errors=["","","",""], infoUser=["","","",""])
    if request.method == 'POST':
        username= request.form["username"]
        password = request.form["password"]
        verifyPassword = request.form["verifyPassword"]
        infoUser =[username,password,verifyPassword]
        errors = validateUserinfo(infoUser)
        if (errors[0] !='') or  (errors[1] !='') or  (errors[2] !='')  :
            return render_template('signup.html',errors=errors, infoUser=infoUser)
        else:
            existing_user = User.query.filter_by(username=username).first()
            if not existing_user:
                new_user = User(username, password)
                db.session.add(new_user)
                db.session.commit()
                session['username'] = username
                return redirect('/newpost', username=username)
            else:
                flash( 'User already exist.  Please log in')
                return redirect('/login')

    return render_template('signup.html')


#Logout route - session ends. 

@app.route('/logout' , methods=['POST'])
def logout():
    del session['username']
    print (username)
    return redirect('/blog')


#route index - Show list of usernames

@app.route('/', methods=['POST', 'GET'])
def index():
    users = User.query.all()
    return render_template ('users.html', users=users)




    


@app.route('/blog', methods=["GET"])
def viewPosts():
    # if session['username']:
    #     id =  request.args.get('id')
    #     posts = Post.query.filter_by(id=id).all()
    #     return render_template('/blog.html', posts=posts)
    # else:
    posts = Post.query.all()
    return render_template('/posts.html',posts=posts ) #,username=username)





@app.route('/newpost', methods=["GET"])
def create():
    owner = User.query.filter_by(username =session['username']).first()
    if owner in session:
        return render_template('newpost.html', username = username)
    else:
        return redirect('/login')

    # posts = Post.query.all()
    # return render_template('posts.html', title=title, content=content)


@app.route('/newpost', methods=['POST'])
def GetContent():
#     if request.method =='GET':
#         username = session['username']
#         return render_template('newpost.html', username=username)
    
    if username in session:
    #owner = User.query.filter_by(username=session['username']).first()
        title= request.form ['title']
        content = request.form ['content']

    if not title:
        flash ("Title can NOT be empty")
        error="error"
        return render_template('newpost.html', content=content)
    if not content:
        flash ("Content can NOT be empty")
        return render_template('newpost.html',title=title)
    #everything is ok, content, title and in session
    else:
        #owner = User.query.filter_by(username = session['username']).first()
        new_post = Post(title,content, owner = user.id)
        db.session.add(new_post)
        db.session.commit()
        #posts = Post.query.all()
        #post_id = new_post.id 
        posts = Post.query.filter_by(id=new_post.id).first()
    
        return render_template('blog_post.html',posts=posts)
    





if __name__ == "__main__":
    app.run()
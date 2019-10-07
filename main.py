from flask import  request, redirect, render_template, flash, session, url_for
from models import User, Post
from app import app, db
from helpers import *



#route login - when a user tries to log in: allow and send to new post or errors flashed, click in signup
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            session['username'] = username
            flash("Logged in")
            return redirect('/newpost')
        else:
            flash('User password incorrect, or user does not exist', 'error')
    return render_template('login.html')


    

        
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
                return redirect('/login')
            else:
                flash( 'User already exist.  Please log in')
                return redirect('/login')

    return render_template('signup.html')


#Logout route - session ends. 

@app.route('/logout')
def logout():
    del session['username']
    return redirect('/')

















#route index - Show list of usernames


@app.route('/', methods=['POST', 'GET'])
def index():
    return redirect("/blog")






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
        owner = User.query (email = session['email']).first()
        new_post = Post(title,content, owner)
        db.session.add(new_post)
        db.session.commit()
        #posts = Post.query.all()
        #post_id = new_post.id 
        posts = Post.query.filter_by(id=new_post.id).first()
        
        return render_template('blog_post.html',posts=posts)
        
        

    
    
    





if __name__ == "__main__":
    app.run()
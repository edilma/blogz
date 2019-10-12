from flask import  request, redirect, render_template, flash, session, url_for
from models import User, Post
from app import app, db
from helpers import *
from hashutils import *

'''Before request decide which routes are allowed to go and post new blogs'''
@app.before_request
def require_login():
    allowed_routes = ['login', 'viewPosts','register','index']
    if request.endpoint not in allowed_routes and 'username' not in session:
        return redirect('/login')

        
'''Route signgup.  Request the user information and verify it using the verifyPassword
function that is located in the helpers.py file. '''
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
            return redirect('/newpost')
        else:
            flash("The username {0} is already registered".format(username), 'danger')
    return redirect('/login')


'''Route login. User that check ok are allowed and send to newpost with session. 
If errors exist, they are flashed. If not username exit redirect to  signup'''
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
            return redirect('/newpost')
        else:
            return redirect ('/signup')


'''Route newpost requires the user to be logged in'''
@app.route('/newpost', methods=['GET','POST'])
def create():
    owner = User.query.filter_by(username=session['username']).first()
    if request.method == 'POST':
        blog_name= request.form['title']
        blog_content = request.form['content']
        isValid = validatePost (blog_name,blog_content)
        if isValid=="ok":
            new_post = Post(blog_name,blog_content,owner)
            db.session.add(new_post)
            db.session.commit()
            posts = Post.query.filter_by(id=new_post.id).first()
            return render_template('blog_post.html',posts=posts)  
        else: 
            flash(isValid) 
            return render_template('newpost.html')
    if request.method == 'GET':
        return render_template('newpost.html')

            
#Logout route - session ends. 

@app.route('/logout' , methods=['GET'])
def logout():
    del session['username']
    print ("logout")
    return redirect('/blog')

'''Route that display the post by user or all'''

@app.route('/blog', methods=["GET"])
def viewPosts():
    #/blog?user=4
    UserId =  request.args.get('user')
    if UserId:
        posts = Post.query.filter_by(owner_id = UserId).all()
        return render_template('/singleUser.html',posts=posts )
    else:
        posts = Post.query.all()
        return render_template('/posts.html',posts=posts)


#route index - Show list of usernames

@app.route('/', methods=['POST', 'GET'])
def index():
    users = User.query.all()
    return render_template ('users.html', users=users)





    

if __name__ == "__main__":
    app.run()
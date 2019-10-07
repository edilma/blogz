from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True
#TODO fix the database conexion
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blogz:edilma@localhost:8889/blogz'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'Lily'
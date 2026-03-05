from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY'] = 'e16f1d19e64364b44b4d5d0c6f803b61'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)

from flaskblog import routes
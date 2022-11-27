import flask
import requests
from flask import url_for, redirect, request, flash
import json
import os 
from random import randint
from dotenv import load_dotenv, find_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user, UserMixin, LoginManager, login_user, login_required, logout_user

load_dotenv(find_dotenv())
    

app = flask.Flask(__name__)
app.secret_key = "flash messages"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view ='login'

@login_manager.user_loader
def load_user(username):
    return Person.query.get(username)

class Person(UserMixin,db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80),unique = True, nullable = False)

        def __repr__(self)-> str:
            return f"Person with Username:{self.username}"
with app.app_context():
    db.create_all()

@app.route('/')
def signup():
    return flask.render_template('signup.html')

@app.route('/signup_post')
def signup_post():
    return flask.render_template('')

@app.route('/login')
def login():
    return flask.render_template('login.html')

@app.route('/login_post')
def login_post():
    return flask.render_template()

@app.route('/home')
def signup_post():
    return flask.render_template('home.html')

@app.route('/random')
def signup_post():
    return flask.render_template('random.html')

if __name__ == "__main__":
    app.run()
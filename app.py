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

@app.route('/signup_post', methods = ['POST','GET'])
def signup_post():
    username=request.form.get('Username')
    person = Person.query.filter_by(username=username).first()
    if person:
        flash("Username already exist login in or create a new user!")
        return redirect(url_for('sign_up'))
    new_user=Person(username=username)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return flask.render_template('login.html')

@app.route('/login_post', methods = ['POST','GET'])
def login_post():
    username = request.form.get('Username')
    person = Person.query.filter_by(username=username).first()
    if person:
        login_user(person)
        return redirect(url_for('home'))
    flash("Username does not exist Sign up or try again!")
    return redirect(url_for('login'))

@app.route('/home')
@login_required
def home():
    return flask.render_template('home.html')

@app.route('/random')
@login_required
def random():
    return flask.render_template('random.html')

if __name__ == "__main__":
    app.run()
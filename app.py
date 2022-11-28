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
        return redirect(url_for('signup'))
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

@app.route('/logout', methods=['POST','GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home', methods = ['POST','GET'])
@login_required
def home():
    search = ''
    return flask.render_template('home.html')

@app.route('/random', methods = ['POST','GET'])
@login_required
def random():
    search = request.form.get('Search')
    SPOON_BASE_URL_AND_PATH = f'https://api.spoonacular.com/food/search'
    response = requests.get(
        SPOON_BASE_URL_AND_PATH,
        params ={
            "apiKey": os.getenv('SPOONAPI'),
            "query": search,
            "number": 10
        }
    )
    name_img = response.json()
    ran_num= randint(0,9)
    recipe = name_img['searchResults'][0]
    recipe_name = recipe['results'][ran_num]['name']
    recipe_img = recipe['results'][ran_num]['image']
    recipe_id = recipe['results'][ran_num]['id']

    id = recipe_id
    SPOON_ING_URL = f'https://api.spoonacular.com/recipes/{id}/information'
    response1 = requests.get(
        SPOON_ING_URL,
        params ={
            "apiKey": os.getenv('SPOONAPI')
        }
    )
    rec_ing = response1.json()
    recipe_ing = rec_ing['extendedIngredients']
    ing = ""
    count = 0
    for i in recipe_ing:
        string = recipe_ing[count]['name']
        strin2 = recipe_ing[count]['measures']['us']['amount']
        string2 = str(strin2)
        string3 = recipe_ing[count]['measures']['us']['unitLong']
        ing = ing + string + " " + string2 + " " + string3 + ", "
        count = count + 1
    ing = ing.rstrip(", ")
    
    SPOON_STEPS_URL = f'https://api.spoonacular.com/recipes/{id}/analyzedInstructions'
    response2 = requests.get(
        SPOON_STEPS_URL,
        params ={
            "apiKey": os.getenv('SPOONAPI')
        }
    )
    rec_steps = response2.json()
    recipe_steps = rec_steps[0]['steps']
    steps = ""
    count1 = 0

    for i in recipe_steps:
        string4 = recipe_steps[count1]['step']
        strin5 = recipe_steps[count1]['number']
        string5 = str(strin5)
        steps = steps + "Step:" + string5 + " " + string4 + ", "
        count1= count1 + 1
    steps = steps.rstrip(", ")
    return flask.render_template('random.html',recipe_name=recipe_name, recipe_img = recipe_img, ing=ing, steps=steps)
if __name__ == "__main__":
    app.run()
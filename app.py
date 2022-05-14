from flask import *;
#from flask import Flask, jsonify
from flask_simple_geoip import SimpleGeoIP
#import sqlite3
#from distutils.log import debug
#from enum import unique
from pyrebase import pyrebase
#from twilio.rest import *
#import random
#from argon2 import hash_password
#import bcrypt
#from django import db
#from flask_sqlalchemy import SQLAlchemy
#from flask_login import UserMixin, login_required, login_user, LoginManager, logout_user, current_user
#from flask_wtf import FlaskForm
#from wtforms import StringField, PasswordField, SubmitField
#from wtforms.validators import InputRequired, Length, ValidationError


"""
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisisasecretkey'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)


class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=30)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Submit")

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()

        if existing_user_username:
            raise ValidationError(
                "That username already exists. Please chosse different one.")


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=30)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Submit")

"""
app = Flask(__name__)
app.secret_key = "super secret key"

config = {
  "apiKey": "AIzaSyBRGnBkPyTq2gDA6bb0hZ5j1qeOcwgWDYE",
  "authDomain": "soumya-f5929.firebaseapp.com",
  "projectId": "soumya-f5929",
  "storageBucket": "soumya-f5929.appspot.com",
  "messagingSenderId": "46421030000",
  "appId": "1:46421030000:web:2d8b68efbf670151a370b5",
  "measurementId": "G-W7WY4R16RH",
  "databaseURL" : ""
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()







@app.route("/")

def index():
    return render_template('index.html')

"""
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)
"""

@app.route("/dashboard", methods=['POST'])
#@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route("/logout", methods=['GET', 'POST'])
#@login_required
def logout():
    auth.current_user = None
    return redirect(url_for('login'))

@app.route("/signup",methods=['GET','POST'])
def signup():
    unsuccessful="User Already exists!"
    if request.method=='POST':
        if request.form.get('id')=='signup':
                   email=request.form['name']
                   password=request.form['pass']
                   try:
                     user=auth.create_user_with_email_and_password(email,password)
                     return redirect(url_for('login'))
                   except:
                     return render_template('register.html',us=unsuccessful)
    return render_template('register.html')
        

@app.route("/login",methods=['GET','POST'])
def login():
    unsuccessful="invalid credentials"
    if request.method=='POST':
        if request.form.get('id')=='login':
            email=request.form['name']
            password=request.form['pass']
            try:
                user=auth.sign_in_with_email_and_password(email,password)
                return render_template('dashboard.html')
            except:
                return render_template('login.html',us=unsuccessful)
        if request.form.get('id')=='forgot':
            email=request.form['name']
            auth.send_password_reset_email(email)
            #flash("Check your email to reset!")
            return redirect(url_for('login'))  
    return render_template('login.html')


"""
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)
"""

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/map")
def map():
    return render_template('map.html')


@app.route("/skinguide")
def skinguide():
    return render_template('skinguide.html')




if __name__ == "__main__":
    app.run(debug=True, port=8000)

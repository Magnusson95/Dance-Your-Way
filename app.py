import os
import boto3
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from werkzeug.security import generate_password_hash, check_password_hash
from passlib.hash import sha256_crypt
from bson.objectid import ObjectId
from botocore.client import Config
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)


ACCESS_KEY_ID = os.environ.get('ACCESS_KEY_ID')
ACCESS_SECRET_KEY = os.environ.get('ACCESS_SECRET_KEY')
app.secret_key = os.environ.get('secret_key')
app.config["MONGO_DBNAME"] = 'events_manager'
app.config["MONGO_URI"] = 'mongodb+srv://prelaunch:prelaunch@danceyourway-fmkw8.mongodb.net/events_manager?retryWrites=true&w=majority'
mongo = PyMongo(app)


class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=20)])
    email = TextField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField(
        'I accept the Terms of Service and Privacy Notice (updated Jan 22, 2015)', [validators.Required()])


@app.route('/')
def home():
    return render_template("index.html", events=mongo.db.events.find())


@app.route('/signup')
def signup():
    if 'logged' in session:
        flash('You are already logged in as ' + session['username'])
        return redirect(url_for('home'))
    return render_template("signup.html")


@app.route('/adduser', methods=['POST', 'GET'])
def adduser():
    organisers = mongo.db.organisers
    find_organiser = organisers.find_one(
        {'username': request.form['username']})

    if find_organiser is None:
        password = generate_password_hash(request.form['password'])
        organisers.insert_one(
            {'username': request.form['username'], 'password': password, 'email': request.form['email']})
        flash('You have registered and are logged in')
        session['username'] = request.form['username']
        session['logged'] = True
        return redirect(url_for('add_event'))
    else:
        flash('Username already exists')
        return redirect(url_for('signup'))


@app.route('/sign-out')
def sign_out():
    '''
    function to allow a user to sign out of the current session
    '''

    session.clear()  # Clear session, notify user and redirect to index
    flash('You are now signed out')
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'logged' in session:
        flash('You are already logged in as ' + session['username'])
        return redirect(url_for('add_event'))

    organisers = mongo.db.organisers
    find_organiser = organisers.find_one(
        {'username': request.form['login_username']})
    if find_organiser:
        if check_password_hash(find_organiser['password'], request.form['login_password']):
            flash('You are logged in as ' + request.form['login_username'])
            session['username'] = request.form['login_username']
            session['logged'] = True
            return redirect(url_for('home'))
        else:
            flash('Incorrect password')
            return redirect(url_for('signup'))
    else:
        flash('Username ' + request.form['login_username'] + ' does not exist')
        return redirect(url_for('signup'))


@app.route('/account')
def account():
    if 'logged' in session:
        current_user = session['username']
        find_user = mongo.db.organisers.find_one({'username': current_user})
        events = mongo.db.events.find({'username': current_user})
        return render_template("account.html", events=events, user=find_user)
    else:
        flash('Please log in to view your account')
        return redirect(url_for('signup'))


@app.route('/get_salsa_events')
def get_salsa_events():
    return render_template("salsa.html", events=mongo.db.events.find())


@app.route('/get_bachata_events')
def get_bachata_events():
    return render_template("bachata.html", events=mongo.db.events.find())


@app.route('/get_kizomba_events')
def get_kizomba_events():
    return render_template("kizomba.html", events=mongo.db.events.find())


@app.route('/style')
def style():
    return render_template("style.html")


@app.route('/add-event')
def add_event():
    if 'logged' in session:
        return render_template("add-event.html", events=mongo.db.events.find())
    else:
        flash('Please log in to add an event')
        return redirect(url_for('signup'))


@app.route('/insert-event', methods=['POST'])
def insert_event():
    events = mongo.db.events
    events.insert_one(request.form.to_dict())
    s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY_ID,
                        aws_secret_access_key=ACCESS_SECRET_KEY)
    s3.Bucket('dance-your-way-event-images').put_object(
        Key=request.form['event_image'], Body=request.files['event_image_s3'])
    return redirect(url_for('event_added'))


@app.route('/event-added')
def event_added():
    return render_template("event-added.html", events=mongo.db.events.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

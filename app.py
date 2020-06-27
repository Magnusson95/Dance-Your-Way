import os
import boto3
import googlemaps
from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for, flash,\
    session
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)


ACCESS_KEY_ID = os.environ.get('ACCESS_KEY_ID')
ACCESS_SECRET_KEY = os.environ.get('ACCESS_SECRET_KEY')
GOOGLE_ACCESS_KEY = os.environ.get('GOOGLE_ACCESS_KEY')
app.secret_key = os.environ.get('secret_key')
app.config["MONGO_DBNAME"] = 'events_manager'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI_KEY")
mongo = PyMongo(app)


@app.route('/')
def home():
    weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday")
    events = mongo.db.events.find(
        {"weekday": weekdays[datetime.now().weekday()]}
    )
    countries = mongo.db.countries.find().sort("country_name")
    return render_template("index.html", events=events, countries=countries)


@app.route('/filtered_index', methods=['POST', 'GET'])
def filtered_index():
    country = request.form["country"]
    weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday")
    events = mongo.db.events.find(
        {
            "weekday": weekdays[datetime.now().weekday()],
            "country": country
        }
    )
    countries = mongo.db.countries.find().sort("country_name")
    return render_template("index.html", events=events, countries=countries)


@app.route('/signup')
def signup():
    if 'logged' in session:
        flash('You are already logged in as ' + session['username'])
        return redirect(url_for('home'))
    return render_template("signup.html")


@app.route('/terms&conditions')
def terms():
    return render_template("terms.html")


@app.route('/adduser', methods=['POST', 'GET'])
def adduser():
    organisers = mongo.db.organisers
    find_organiser = organisers.find_one(
        {'username': request.form['username']})

    if find_organiser is None:
        password = generate_password_hash(request.form['password'])
        organisers.insert_one(
            {
                'username': request.form['username'],
                'password': password,
                'email': request.form['email'],
                't&c': request.form['t&c']
            })
        flash
        (
            'You have registered and are logged in. Welcome '
            + request.form['username']
        )
        session['username'] = request.form['username']
        session['logged'] = True
        return redirect(url_for('account'))
    else:
        flash('Username already exists')
        return redirect(url_for('signup'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'logged' in session:
        flash('Welcome back ' + session['username'])
        return redirect(url_for('add_event'))

    organisers = mongo.db.organisers
    find_organiser = organisers.find_one(
        {'username': request.form['login_username']})
    if find_organiser:
        if check_password_hash(
            find_organiser['password'],
            request.form['login_password']
        ):
            flash('Welcome back ' + request.form['login_username'])
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
        countries = mongo.db.countries.find().sort("country_name")
        return render_template(
            "account.html",
            events=events,
            user=find_user,
            countries=countries
        )
    else:
        flash('Please log in to view your account')
        return redirect(url_for('signup'))


@app.route('/sign-out')
def sign_out():
    '''
    function to allow a user to sign out of the current session
    '''

    session.clear()  # Clear session, notify user and redirect to index
    flash('You are now signed out')
    return redirect(url_for('home'))


@app.route('/edituser/<organiser_username>', methods=['POST'])
def edituser(organiser_username):
    organisers = mongo.db.organisers
    organisers.update({"username": organiser_username},
                      {
        'facebook': request.form.get('facebook'),
        'mobile': request.form.get('mobile'),
        'email': request.form.get('email'),
        'password': request.form.get('password'),
        'username': request.form.get('username'),
        'event_image': request.form.get('event_image'),
        'about': request.form.get('about'),
        'city': request.form.get('city'),
        'country': request.form.get('country'),
    }
    )
    if request.form.get('image-check') == "no change":
        flash('You have updated your details')
        return redirect(url_for('account'))
    else:
        s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY_ID,
                            aws_secret_access_key=ACCESS_SECRET_KEY)
        s3.Bucket('dance-your-way-event-images').put_object(
            Key=request.form['event_image'],
            Body=request.files['event_image_s3'])
        flash('You have updated your details')
        return redirect(url_for('account'))


@app.route('/delete_profile/<organiser_id>')
def delete_profile(organiser_id):
    mongo.db.organisers.remove({'_id': ObjectId(organiser_id)})
    return redirect(url_for('sign_out'))


@app.route('/add-event')
def add_event():
    if 'logged' in session:
        current_user = session['username']
        find_user = mongo.db.organisers.find_one({'username': current_user})
        countries = mongo.db.countries.find().sort("country_name")
        return render_template(
            "add-event.html",
            events=mongo.db.events.find(),
            user=find_user, countries=countries
        )
    else:
        flash('Please log in to add an event')
        return redirect(url_for('signup'))


@app.route('/insert-event', methods=['POST'])
def insert_event():
    events = mongo.db.events
    gmaps_key = googlemaps.Client(key=GOOGLE_ACCESS_KEY)
    geocode_result = gmaps_key.geocode(request.form.get('address'))
    lat = geocode_result[0]["geometry"]["location"]["lat"]
    lon = geocode_result[0]["geometry"]["location"]["lng"]
    newEvent = events.insert_one(request.form.to_dict())
    events.update_one(
        {"_id": ObjectId(newEvent.inserted_id)},
        {"$set": {"lat": lat, "lon": lon}}
    )
    s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY_ID,
                        aws_secret_access_key=ACCESS_SECRET_KEY)
    s3.Bucket('dance-your-way-event-images').put_object(
        Key=request.form['event_image'], Body=request.files['event_image_s3'])
    flash("You have successfully added an event")
    return redirect(url_for('account'))


@app.route('/edit_event/<event_id>')
def edit_event(event_id):
    the_event = mongo.db.events.find_one({"_id": ObjectId(event_id)})
    current_user = session['username']
    find_user = mongo.db.organisers.find_one({'username': current_user})
    countries = mongo.db.countries.find().sort("country_name")
    return render_template(
        "edit-event.html",
        user=find_user,
        event=the_event,
        countries=countries
    )


@app.route('/update_event/<event_id>', methods=['POST'])
def update_event(event_id):
    events = mongo.db.events
    events.update({"_id": ObjectId(event_id)}, {
        'username': request.form.get('username'),
        'event_name': request.form.get('event_name'),
        'address': request.form.get('address'),
        'event_link': request.form.get('event_link'),
        'event_description': request.form.get(
            'event_description'
        ),
        'weekday': request.form.get('weekday'),
        'time': request.form.get('time'),
        'price': request.form.get('price'),
        'event_image': request.form.get('event_image'),
        'salsa': request.form.get('salsa'),
        'bachata': request.form.get('bachata'),
        'kizomba': request.form.get('kizomba'),
        'city': request.form.get('city'),
        'country': request.form.get('country')
    }
    )
    if request.form.get('image-check') == "no change":
        flash('You have updated your event')
        return redirect(url_for('account'))
    else:
        s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY_ID,
                            aws_secret_access_key=ACCESS_SECRET_KEY)
        s3.Bucket('dance-your-way-event-images').put_object(
            Key=request.form['event_image'],
            Body=request.files['event_image_s3'])
        flash('You have updated your event')
        return redirect(url_for('account'))


@app.route('/delete_event/<event_id>')
def delete_event(event_id):
    mongo.db.events.remove({'_id': ObjectId(event_id)})
    flash('Your event has now been removed')
    return redirect(url_for('account'))


@app.route('/style')
def style():
    return render_template("style.html")


@app.route('/get_salsa_events')
def get_salsa_events():
    return render_template("salsa.html", events=mongo.db.events.find())


@app.route('/get_bachata_events')
def get_bachata_events():
    return render_template("bachata.html", events=mongo.db.events.find())


@app.route('/get_kizomba_events')
def get_kizomba_events():
    return render_template("kizomba.html", events=mongo.db.events.find())


@app.route('/get_organisers')
def get_organisers():
    organiser = mongo.db.organisers.find().sort("username")
    events = mongo.db.events.find()
    return render_template(
        "all-organisers.html",
        organiser=organiser,
        events=list(events)
    )


@app.route('/organiser/<organiser_username>')
def organiser(organiser_username):
    _organiser = mongo.db.organisers.find_one({"username": organiser_username})
    _event = mongo.db.events.find({"username": organiser_username})
    return render_template(
        "organiser.html",
        organiser=_organiser, events=_event)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

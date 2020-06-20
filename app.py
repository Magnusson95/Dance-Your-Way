import os
import googlemaps
from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'events_manager'
app.config["MONGO_URI"] = 'mongodb+srv://prelaunch:prelaunch@danceyourway-fmkw8.mongodb.net/events_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)


gmaps = googlemaps.Client(key='AIzaSyCWZTBCpz1s2iN98QZxLZd_pBmYWWu1kUs')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')


@app.route('/')
def home():
    return render_template("index.html", events=mongo.db.events.find())


@app.route('/get_events')
def get_events():
    return render_template("events.html", events=mongo.db.events.find())


@app.route('/style')
def style():
    return render_template("style.html")


@app.route('/add-event')
def add_event():
    return render_template("add-event.html", events=mongo.db.events.find())


@app.route('/test')
def test():
    return render_template("test.html")


@app.route('/insert-event', methods=['POST'])
def insert_event():
    events = mongo.db.events
    events.insert_one(request.form.to_dict())
    return redirect(url_for('get_events'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)


# Geocode request: https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyCWZTBCpz1s2iN98QZxLZd_pBmYWWu1kUs

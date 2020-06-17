import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'events_manager'
app.config["MONGO_URI"] = 'mongodb+srv://prelaunch:prelaunch@danceyourway-fmkw8.mongodb.net/events_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
def home():
    return render_template("index.html", events=mongo.db.events.find())

@app.route('/get_events')
def get_events():
    return render_template("events.html", events=mongo.db.events.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

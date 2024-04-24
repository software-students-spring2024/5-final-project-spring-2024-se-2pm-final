import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
import flask
import pymongo
import certifi
from bson.objectid import ObjectId
from dotenv import load_dotenv
import calendar
from datetime import datetime, timedelta
import flask_login
from werkzeug.security import generate_password_hash, check_password_hash
load_dotenv()
app = Flask(__name__)
#log in
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
cxn = pymongo.MongoClient(os.getenv("MONGO_URI"), tlsCAFile=certifi.where())
db = cxn[str(os.getenv("MONGO_DBNAME"))]
try:
    cxn.admin.command("ping")
    print(" *", "Connected to MongoDB!")
except Exception as e:
     print(" * MongoDB connection error:", e)
def readCounter():
    counterSetting = db['settings'].find_one({'setting': 'counter'})
    if counterSetting:
        return int(counterSetting['value'])
    return 0

#potential taskId generation
def writeCounter(counter):
    db['settings'].update_one({'setting': 'counter'}, {
                              '$set': {'value': counter}})
class User(flask_login.UserMixin):
    def __init__(self, user_id):
        self.id = user_id

#connection
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
# python3 quiz-app/app.py to run
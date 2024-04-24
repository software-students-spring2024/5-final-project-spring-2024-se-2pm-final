import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
import flask
from pymongo import MongoClient
import certifi
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# load environment variables
# mongo_uri = os.environ.get("MONGO_URI")
flask_port = os.environ.get("FLASK_RUN_PORT")
MONGO_HOST = os.environ.get("DB_HOST", "mongodb_server")

# Load environment variables for MongoDB connection
MONGO_PORT = os.environ.get("MONGO_PORT", 27017)
MONGO_DB = os.environ.get("MONGO_DB", "quiz_db")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
mongo_uri = f"mongodb://{DB_USER}:{DB_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}"
client = MongoClient(mongo_uri)
db = client.get_database(MONGO_DB)
quiz_collection = db["quizzes"]
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
# python3 quiz-app/app.py to run
import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
import flask
import pymongo
import certifi
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
cxn = pymongo.MongoClient(os.getenv("MONGO_URI"), tlsCAFile=certifi.where())
db = cxn[str(os.getenv("MONGO_DBNAME"))]
try:
    cxn.admin.command("ping")
    print(" *", "Connected to MongoDB!")
except Exception as e:
     print(" * MongoDB connection error:", e)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
# python3 quiz-app/app.py to run
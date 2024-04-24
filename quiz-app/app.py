import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
import flask
import pymongo
import certifi
from bson.objectid import ObjectId
from dotenv import load_dotenv

# load env variables
load_dotenv()

# initialize app and db connection
app = Flask(__name__)

cxn = pymongo.MongoClient(os.getenv("MONGO_URI"), tlsCAFile=certifi.where())
db = cxn[str(os.getenv("MONGO_DBNAME"))]

try:
    cxn.admin.command("ping")
    print(" *", "Connected to MongoDB!")
except Exception as e:
     print(" * MongoDB connection error:", e)

# home route. Displays a simple home page.
@app.route('/')
def home():
    quizzes = db.quizzes.find()
    return render_template('index.html', quizzes=quizzes)

# quiz route
@app.route('/quiz/<quiz_id>')
def quiz(quiz_id):
    # fetch quiz by id
    quiz = db.quizzes.find_one({'_id': ObjectId(quiz_id)})
    return render_template('quiz.html', quiz=quiz)

# submit route
@app.route('/submit_quiz/<quiz_id>', methods=['POST'])
def submit_quiz(quiz_id):
    # counter correct answers and present score
    answers = request.form.to_dict()
    correct_answers = db.quizzes.find_one({'_id': ObjectId(quiz_id)})['answers']
    score = sum(1 for question, answer in answers.items() if correct_answers.get(question) == answer)
    return render_template('result.html', score=score)

if __name__ == '__main__':
    app_port = os.getenv("FLASK_PORT", "3000")
    app.run(debug=True, port=app_port)
# python3 quiz-app/app.py to run
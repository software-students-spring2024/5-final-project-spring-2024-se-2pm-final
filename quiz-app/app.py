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

# get route for creating a quiz
@app.route('/create', methods=['GET'])
def create_quiz():
    return render_template('create.html')

# get post for creating a quiz
@app.route('/create', methods=['POST'])
def add_quiz():
    title = request.form.get('title')
    questions = {}
    answers = {}
    
    i = 1
    while True:
        question = request.form.get(f'question{i}')
        answer = request.form.get(f'answer{i}')
        options_str = request.form.get(f'options{i}')
        if not question or not answer or not options_str:
            break
        options = [option.strip() for option in options_str.split(',')]
        questions[question] = options
        answers[question] = answer
        i += 1

    # insert new quiz
    quiz = {
        'title': title,
        'questions': questions,
        'answers': answers
    }
    db.quizzes.insert_one(quiz)
    return redirect(url_for('home'))

@app.route("/delete", methods=['GET', 'POST'])
def delete():
    # POST handler
    if request.method == 'POST':

        # get taskId
        quiz_ids = request.form.getlist('quiz_ids[]')

        # delete
        if quiz_ids:
            for quiz_id in quiz_ids:
                db.quizzes.delete_one({'_id': ObjectId(quiz_id)})

        # refresh
        return redirect(url_for('delete'))

    # display delete template
    quizzes = list(db.quizzes.find())
    return render_template('delete.html', quizzes =quizzes)


if __name__ == '__main__':
    app_port = os.getenv("FLASK_PORT", "3000")
    app.run(debug=True, port=app_port)
# python3 quiz-app/app.py to run
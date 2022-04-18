from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

# DATA

quiz_questions = {
    "0" : {"difficulty" : "Easy",
    "number": "1",
    "transcription": "–  ·–   –·",
    "audio_src": "somelink",
    "next_question": "1",
    "question_type" : "morse_english",
    "word" : "TAN",
    "answer" : "TAN"
    },
    "1" : {"difficulty" : "Easy",
    "number": "2",
    "transcription": "--. .. -.",
    "audio_src": "somelink",
    "next_question": "2",
    "question_type" : "sound_morse",
    "word" : "DONE",
    "answer" : "--. .. -."
    },
    "2" : {"difficulty" : "Easy",
    "number": "3",
    "transcription": "-.. --- -. .",
    "audio_src": "somelink",
    "next_question": "end",
    "question_type" : "english_morse",
    "word" : "DONE",
    "answer" : "-.. --- -. ."
    }
}

quiz_answers = {}

score = 0

# ROUTES
@app.route('/')
def home():
    return render_template('home.html')  

@app.route('/learn')
def letters():
    global letters
    return render_template('letter.html', data=letters)

@app.route('/learn/numbers')
def numbers():
    global numbers
    return render_template('numbers.html', data=numbers)

@app.route('/learn/<id>')
def learn(id=None):
    letter = data[id]
    return render_template('learn.html', data=letter) 

@app.route('/quiz/<id>')
def quiz(id=None):
    question = quiz_questions[id]
    return render_template('quiz.html', question=question) 

@app.route('/quiz/end')
def end():
    return render_template('end.html', score=score) 


# AJAX FUNCTIONS
@app.route('/quiz/save_score', methods=['GET', 'POST'])
def save_score():
    global score
    json_data = request.get_json()
    score = json_data["score"]
    return jsonify(score=score)

@app.route('/quiz/check_answer', methods=['GET', 'POST'])
def check_answer():
    global score
    json_data = request.get_json()
    ans = json_data["answer"]
    qid = json_data["question_id"]
    correct = 0
    if(ans == quiz_questions[str(qid)]["answer"]):
        correct = 1
    score += correct
    return jsonify(correct=correct)


if __name__ == '__main__':
   app.run(debug = True)





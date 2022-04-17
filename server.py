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
    "question_type" : "0",
    "answer" : "idk"
    },
    "1" : {"difficulty" : "Easy",
    "number": "2",
    "transcription": "--. .. -.",
    "audio_src": "somelink",
    "next_question": "2",
    "question_type" : "1",
    "answer" : "idk"
    },
    "2" : {"difficulty" : "Easy",
    "number": "3",
    "transcription": "-.. --- -. .",
    "audio_src": "somelink",
    "next_question": "end",
    "question_type" : "2",
    "answer" : "idk"
    }
}

quiz_answers = {}



# ROUTES
@app.route('/')
def home():
    return render_template('home.html')  

@app.route('/learn/<id>')
def learn(id=None):
    return render_template('learn.html', data={"id": id}) 

@app.route('/quiz/<id>')
def quiz(id=None):
    question = quiz_questions[id]
    return render_template('quiz.html', question=question) 

@app.route('/quiz/end')
def end():
    return render_template('end.html') 


# AJAX FUNCTIONS


if __name__ == '__main__':
   app.run(debug = True)





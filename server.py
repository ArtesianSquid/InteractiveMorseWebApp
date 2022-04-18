from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

# DATA

alphabet = {
    "1": {
        "id": "1",
        "letter": "A",
        "morse": "· –",
        "word1": "BAT",
        "morse1": "–···  ·–    –",
        "word2": "ANT",
        "morse2": "·–  –·  –",
        "word3": "CANDY",
        "morse3": "–·–·   ·–   –·  –·· –·– –",
        "next_lesson": "4"
    },
    "2": {
        "id": "2",
        "letter": "B",
        "morse": "– · · ·"
    },
    "3": {
        "id": "3",
        "letter": "C",
        "morse": "– · – ·"
    },
    "4": {
        "id": "4",
        "letter": "D",
        "morse": "– · ·",
        "word1": "LAD",
        "morse1": "·–··  ·–  –··",
        "word2": "OLD",
        "morse2": "– – –  ·–··  –··",
        "word3": "FRIED",
        "morse3": "··–·  ·–·  ··  ·  –··",
        "next_lesson": "5"
    },
    "5": {
        "id": "5",
        "letter": "E",
        "morse": "·",
        "word1": "ALE",
        "morse1": "·–  ·–··  ·",
        "word2": "EEL",
        "morse2": "·  ·  ·–··",
        "word3": "ANGER",
        "morse3": "·–  –·  – –·  ·  ·–·",
        "next_lesson": "8"
    },
    "6": {
        "id": "6",
        "letter": "F",
        "morse": "· · – ·"
    },
    "7": {
        "id": "7",
        "letter": "G",
        "morse": "– – ·"
    },
    "8": {
        "id": "8",
        "letter": "H",
        "morse": "····",
        "word1": "HUG",
        "morse1": "····  ··–  – –·",
        "word2": "THE",
        "morse2": "–  ····  ·",
        "word3": "TRASH",
        "morse3": "–  ·–·  ·–  ···  ····",
        "next_lesson": "9" 
    },
    "9": {
        "id": "9",
        "letter": "I",
        "morse": "··",
        "word1": "FIG",
        "morse1": "··–·  ··  – –·",
        "word2": "IKE",
        "morse2": "··  –·–  ·",
        "word3": "SLICE",
        "morse3": "···  ·–··  ··  –·–·  ·",
        "next_lesson": "14"
    },
    "10": {
        "id": "10",
        "letter": "J",
        "morse": "· – – –"
    },
    "11": {
        "id": "11",
        "letter": "K",
        "morse": "– · – ·"
    },
    "12": {
        "id": "12",
        "letter": "L",
        "morse": "· – · ·"
    },
    "13": {
        "id": "13",
        "letter": "M",
        "morse": "– –"
    },
    "14": {
        "id": "14",
        "letter": "N",
        "morse": "– ·",
        "word1": "PIN",
        "morse1": "·– –·  ··  –·",
        "word2": "ONE",
        "morse2": "– – –  –·  ·",
        "word3": "PRANK",
        "morse3": "·– –·  ·–·  ·–  –·  –·–",
        "next_lesson": "end"
    },
    "15": {
        "id": "15",
        "letter": "O",
        "morse": "0"
    },
    "16": {
        "id": "16",
        "letter": "P",
        "morse": "0"
    },
    "17": {
        "id": "17",
        "letter": "Q",
        "morse": "0"
    },
    "18": {
        "id": "18",
        "letter": "R",
        "morse": "0"
    },
    "19": {
        "id": "19",
        "letter": "S",
        "morse": "0"
    },
    "20": {
        "id": "20",
        "letter": "T",
        "morse": "0"
    },
    "21": {
        "id": "21",
        "letter": "U",
        "morse": "0"
    },
    "22": {
        "id": "22",
        "letter": "V",
        "morse": "0"
    },
    "23": {
        "id": "23",
        "letter": "W",
        "morse": "0"
    },
    "24": {
        "id": "24",
        "letter": "X",
        "morse": "0"
    },
    "25": {
        "id": "25",
        "letter": "Y",
        "morse": "0"
    },
    "26": {
        "id": "26",
        "letter": "Z",
        "morse": "0"
    }
} 

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
    global alphabet
    return render_template('letter.html', data=alphabet)

@app.route('/learn/numbers')
def numbers():
    # alpahbet will be replaced by the dictionary for nums later
    global nums
    nums = alphabet
    return render_template('numbers.html', data=nums)

@app.route('/learn/<id>')
def learn(id=None):
    letter = alphabet[id]
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





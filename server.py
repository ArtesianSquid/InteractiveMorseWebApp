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
        "morse": "– · · ·",
        "next_lesson": "4"
    },
    "3": {
        "id": "3",
        "letter": "C",
        "morse": "– · – ·",
        "next_lesson": "4"
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
        "morse": "· · – ·",
        "next_lesson": "8"
    },
    "7": {
        "id": "7",
        "letter": "G",
        "morse": "– – ·",
        "next_lesson": "8"
    },
    "8": {
        "id": "8",
        "letter": "H",
        "morse": "· · · ·",
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
        "morse": "· ·",
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
        "morse": "· – – –",
        "next_lesson": "14"
    },
    "11": {
        "id": "11",
        "letter": "K",
        "morse": "– · – ·",
        "next_lesson": "14"
    },
    "12": {
        "id": "12",
        "letter": "L",
        "morse": "· – · ·",
        "next_lesson": "14"
    },
    "13": {
        "id": "13",
        "letter": "M",
        "morse": "– –",
        "next_lesson": "14"
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
        "next_lesson": "15"
    },
    "15": {
        "id": "15",
        "letter": "O",
        "morse": "– – –",
        "word1": "DOG",
        "morse1": "–··  – – –  – –·",
        "word2": "COP",
        "morse2": "–·–·  – – –  ·– –·",
        "word3": "FLOOR",
        "morse3": "··–·  ·–··  – – –  – – –  ·–·",
        "next_lesson": "18"
    },
    "16": {
        "id": "16",
        "letter": "P",
        "morse": "· – – ·",
        "next_lesson": "18"
    },
    "17": {
        "id": "17",
        "letter": "Q",
        "morse": "– – · –",
        "next_lesson": "18"
    },
    "18": {
        "id": "18",
        "letter": "R",
        "morse": "· – ·",
        "word1": "RAW",
        "morse1": "·–·  ·–  ·– –",
        "word2": "BAR",
        "morse2": "-···  ·–  ·–·",
        "word3": "HERO",
        "morse3": "····  ·  ·–·  – – –",
        "next_lesson": "19"
    },
    "19": {
        "id": "19",
        "letter": "S",
        "morse": "· · ·",
        "word1": "USE",
        "morse1": "··–  ···  ·",
        "word2": "ASH",
        "morse2": "·-  ···  ····",
        "word3": "OASIS",
        "morse3": "·– – –  ·– ···  ··  ···",
        "next_lesson": "20"
    },
    "20": {
        "id": "20",
        "letter": "T",
        "morse": "–",
        "word1": "EAT",
        "morse1": "·  ·–  –",
        "word2": "TAP",
        "morse2": "–  ·–  ·– –·",
        "word3": "DATE",
        "morse3": "–··  ·–  –  ·",
        "next_lesson": "1"
    },
    "21": {
        "id": "21",
        "letter": "U",
        "morse": "· · –",
        "next_lesson": "1"
    },
    "22": {
        "id": "22",
        "letter": "V",
        "morse": "· · · –",
        "next_lesson": "1"
    },
    "23": {
        "id": "23",
        "letter": "W",
        "morse": "· – –",
        "next_lesson": "1"
    },
    "24": {
        "id": "24",
        "letter": "X",
        "morse": "– · · –",
        "next_lesson": "1"
    },
    "25": {
        "id": "25",
        "letter": "Y",
        "morse": "– · – –",
        "next_lesson": "1"
    },
    "26": {
        "id": "26",
        "letter": "Z",
        "morse": "– – · ·",
        "next_lesson": "1"
    }
}

nums = {
    "1": {
        "id": "1",
        "char": "1",
        "morse": "· – – – –"
    },
    "2": {
        "id": "2",
        "char": "2",
        "morse": "· · – – –"
    },
    "3": {
        "id": "3",
        "char": "3",
        "morse": "· · · – –"
    },
    "4": {
        "id": "4",
        "char": "4",
        "morse": "· · · · –"
    },
    "5": {
        "id": "5",
        "char": "5",
        "morse": "· · · · ·"
    },
    "6": {
        "id": "6",
        "char": "6",
        "morse": "– · · · ·"
    },
    "7": {
        "id": "7",
        "char": "7",
        "morse": "– – · · ·"
    },
    "8": {
        "id": "8",
        "char": "8",
        "morse": "– – – · ·"
    },
    "9": {
        "id": "9",
        "char": "9",
        "morse": "– – – – ·"
    },
    "10": {
        "id": "10",
        "char": "0",
        "morse": "– – – – –"
    },
    "11": {
        "id": "11",
        "char": ".",
        "morse": "· – · – · –"
    },
    "12": {
        "id": "12",
        "char": ",",
        "morse": "– - · · – –"
    },
    "13": {
        "id": "13",
        "char": "?",
        "morse": "· · – – · ·"
    },
    "14": {
        "id": "14",
        "char": "/",
        "morse": "– · · – ·"
    }
}


quiz_questions = {
    "0" : {"difficulty" : "Easy",
    "number": "1",
    "transcription": "–  ·–   –·",
    "audio_src": "somelink",
    "next_question": "1",
    "prev_question": "-1",
    "question_type" : "morse_english",
    "word" : "TAN",
    "answer" : "TAN",
    },
    "1" : {"difficulty" : "Easy",
    "number": "2",
    "transcription": "--. .. -.",
    "audio_src": "somelink",
    "next_question": "2",
    "prev_question": "0",
    "question_type" : "sound_morse",
    "word" : "DONE",
    "answer" : "--. .. -."
    },
    "2" : {"difficulty" : "Easy",
    "number": "3",
    "transcription": "-.. --- -. .",
    "audio_src": "somelink",
    "next_question": "end",
    "prev_question": "1",
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

@app.route('/quiz_home')
def quiz_home():
    return render_template('quiz_home.html') 


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

@app.route('/not_implemented')
def not_implemented():
    return render_template('not_implemented.html')  


if __name__ == '__main__':
   app.run(debug = True)





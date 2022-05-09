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
        "word1": "BAT",
        "morse1": "–···  ·–    –",
        "word2": "TAB",
        "morse2": "–   ·–   –···",
        "word3": "ABOUT",
        "morse3": "·–   –···   – – –   · · –   –",
        "next_lesson": "4"
    },
    "3": {
        "id": "3",
        "letter": "C",
        "morse": "– · – ·",
        "word1": "CAT",
        "morse1": "–·–·  ·–    –",
        "word2": "CAB",
        "morse2": "–·–·   ·–   –···",
        "word3": "CANDY",
        "morse3": "–·–·   ·–   –·  –·· –·– –",
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
        "word1": "FEE",
        "morse1": "··–·  ·   ·",
        "word2": "ELF",
        "morse2": "·  ·–·· ··–·",
        "word3": "FINDS",
        "morse3": "··–·  ··  –·  –··  ···",
        "next_lesson": "8"
    },
    "7": {
        "id": "7",
        "letter": "G",
        "morse": "– – ·",
        "word1": "LAG",
        "morse1": "·–··  ·–   – –·",
        "word2": "GEL",
        "morse2": "– –·   ·   ·–··",
        "word3": "GLAND",
        "morse3": "– –·   ·–··   ·–   –·   –··",
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
        "word1": "JAM",
        "morse1": "·– – –   ·–   – –",
        "word2": "JUG",
        "morse2": "·– – –   ··–   – –·",
        "word3": "JAILS",
        "morse3": "·– – –  ·–  ··  ·–··  ···",
        "next_lesson": "14"
    },
    "11": {
        "id": "11",
        "letter": "K",
        "morse": "– · – ·",
        "word1": "KAT",
        "morse1": "–·–·   ·–   –",
        "word2": "KEG",
        "morse2": "–·–·   ·   – –·",
        "word3": "ANKLE",
        "morse3": "·–   –·   –·–·  ·–··   ·",
        "next_lesson": "14"
    },
    "12": {
        "id": "12",
        "letter": "L",
        "morse": "· – · ·",
        "word1": "LED",
        "morse1": "·–··   ·   –··",
        "word2": "LAG",
        "morse2": "·–··   ·–   – –·",
        "word3": "ANKLE",
        "morse3": "·–   –·   –·–·  ·–··   ·",
        "next_lesson": "14"
    },
    "13": {
        "id": "13",
        "letter": "M",
        "morse": "– –",
        "word1": "MAD",
        "morse1": "– –   ·–   –··",
        "word2": "LAM",
        "morse2": "·–··   ·–   – –",
        "word3": "AMPLE",
        "morse3": "·–   – –   ·– –·  ·–··   ·",
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
        "word1": "PAD",
        "morse1": "·– –·   ·–   –··",
        "word2": "LIP",
        "morse2": "·–··   ··   ·– –·",
        "word3": "AMPLE",
        "morse3": "·–   – –   ·– –·  ·–··   ·",
        "next_lesson": "18"
    },
    "17": {
        "id": "17",
        "letter": "Q",
        "morse": "– – · –",
        "word1": "QUIT",
        "morse1": "– –·–   ··–   ··   –",
        "word2": "QUAD",
        "morse2": "– –·–   ··–   ·–   –··",
        "word3": "QUILT",
        "morse3": "– –·–   ··–   ··   ·–··   –",
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
        "word1": "MUG",
        "morse1": "– –   ··–   – –·",
        "word2": "PUN",
        "morse2": "·– –·  ··–  –·",
        "word3": "QUILT",
        "morse3": "– –·–   ··–   ··   ·–··   –",
        "next_lesson": "1"
    },
    "22": {
        "id": "22",
        "letter": "V",
        "morse": "· · · –",
        "word1": "VAT",
        "morse1": "···–   ·–   –",
        "word2": "LUV",
        "morse2": "·–··  ··–  ···–",
        "word3": "VAULT",
        "morse3": "···–   ·–   ··–   ·–··   –",
        "next_lesson": "1"
    },
    "23": {
        "id": "23",
        "letter": "W",
        "morse": "· – –",
        "word1": "WET",
        "morse1": "·– –   ·   –",
        "word2": "PEW",
        "morse2": "·– –·  ·  ·– –",
        "word3": "WAITS",
        "morse3": "·– –   ·–   ··   –   ···",
        "next_lesson": "1"
    },
    "24": {
        "id": "24",
        "letter": "X",
        "morse": "– · · –",
        "word1": "BOX",
        "morse1": "–···   – – –   –··–",
        "word2": "AXE",
        "morse2": "·–  –··–  ·",
        "word3": "PIXIE",
        "morse3": "·– –·   ··   –··–   ··   ·",
        "next_lesson": "1"
    },
    "25": {
        "id": "25",
        "letter": "Y",
        "morse": "– · – –",
        "word1": "YAM",
        "morse1": "–·– –   ·–   – –",
        "word2": "AYE",
        "morse2": "·–  –·– ·  ·",
        "word3": "SHYLY",
        "morse3": "···   ····   –·– –   ·–··   –·– –",
        "next_lesson": "1"
    },
    "26": {
        "id": "26",
        "letter": "Z",
        "morse": "– – · ·",
        "word1": "ZOO",
        "morse1": "– –··   – – –   – – –",
        "word2": "ZIT",
        "morse2": "– –··  ··  –",
        "word3": "ZEBRA",
        "morse3": "– –··   ·   –···   ·–·   ·–",
        "next_lesson": "1"
    }
}

nums = {
    "1": {
        "id": "1",
        "char": "1",
        "audio": "1.wav",
        "morse": "· – – – –"
    },
    "2": {
        "id": "2",
        "char": "2",
        "audio": "2.wav",
        "morse": "· · – – –"
    },
    "3": {
        "id": "3",
        "char": "3",
        "audio": "3.wav",
        "morse": "· · · – –"
    },
    "4": {
        "id": "4",
        "char": "4",
        "audio": "4.wav",
        "morse": "· · · · –"
    },
    "5": {
        "id": "5",
        "char": "5",
        "audio": "5.wav",
        "morse": "· · · · ·"
    },
    "6": {
        "id": "6",
        "char": "6",
        "audio": "6.wav",
        "morse": "– · · · ·"
    },
    "7": {
        "id": "7",
        "char": "7",
        "audio": "7.wav",
        "morse": "– – · · ·"
    },
    "8": {
        "id": "8",
        "char": "8",
        "audio": "8.wav",
        "morse": "– – – · ·"
    },
    "9": {
        "id": "9",
        "char": "9",
        "audio": "9.wav",
        "morse": "– – – – ·"
    },
    "10": {
        "id": "10",
        "char": "0",
        "audio": "0.wav",
        "morse": "– – – – –"
    },
    "11": {
        "id": "11",
        "char": ".",
        "audio": "..wav",
        "morse": "· – · – · –"
    },
    "12": {
        "id": "12",
        "char": ",",
        "audio": ",.wav",
        "morse": "– - · · – –"
    },
    "13": {
        "id": "13",
        "char": "?",
        "audio": "question_mark.wav",
        "morse": "· · – – · ·"
    },
    "14": {
        "id": "14",
        "char": "/",
        "audio": "back_slash.wav",
        "morse": "– · · – ·"
    }
}


quiz_questions = {
    "0" : {"id":"0",
    "difficulty" : "Easy",
    "number": "1",
    "transcription": "–  ·–   –·",
    "audio_src": "TAN.wav",
    "next_question": "1",
    "prev_question": "-1",
    "question_type" : "morse_english",
    "word" : "TAN",
    "answer" : "TAN",
    "answered" : False,
    },
    "1" : {"id":"1",
    "difficulty" : "Easy",
    "number": "2",
    "transcription": "····  ··  –··",
    "audio_src": "HID.wav",
    "next_question": "2",
    "prev_question": "0",
    "question_type" : "morse_english",
    "word" : "HID",
    "answer" : "HID",
    "answered" : False,
    },
    "2" : {"id":"2",
    "difficulty" : "Easy",
    "number": "3",
    "transcription": "·  –·  –··",
    "audio_src": "END.wav",
    "next_question": "3",
    "prev_question": "1",
    "question_type" : "sound_morse",
    "word" : "END",
    "answer" : "·  –·  –··",
    "answered" : False,
    },
    "3" : {"id":"3",
    "difficulty" : "Easy",
    "number": "4",
    "transcription": "--. .. -.",
    "audio_src": "somelink",
    "next_question": "4",
    "prev_question": "2",
    "question_type" : "english_morse",
    "word" : "DONE",
    "answer" : "-.. --- -. .",
    "answered" : False,
    },
    "4" : {"id":"4",
    "difficulty" : "Easy",
    "number": "5",
    "transcription": "-.. --- -. .",
    "audio_src": "somelink",
    "next_question": "end",
    "prev_question": "3",
    "question_type" : "english_morse",
    "word" : "DASH",
    "answer" : "-.. .- ... ....",
    "answered" : False,
    },
    "5" : {"id":"5",
    "difficulty" : "Medium",
    "number": "1",
    "transcription": "-.-. .- .-. -",
    "audio_src": "CART.wav",
    "next_question": "6",
    "prev_question": "-1",
    "question_type" : "morse_english",
    "word" : "CART",
    "answer" : "CART",
    "answered" : False,
    },
    "6" : {"id":"6",
    "difficulty" : "Medium",
    "number": "2",
    "transcription": "--.. .- -.-. -.-",
    "audio_src": "ZACK.wav",
    "next_question": "7",
    "prev_question": "6",
    "question_type" : "morse_english",
    "word" : "ZACK",
    "answer" : "ZACK",
    "answered" : False,
    },
    "7" : {"id":"7",
    "difficulty" : "Medium",
    "number": "3",
    "transcription": ".-- .- ...- -.--",
    "audio_src": "WAVY.wav",
    "next_question": "8",
    "prev_question": "6",
    "question_type" : "sound_morse",
    "word" : "WAVY",
    "answer" : ".-- .- ...- -.--",
    "answered" : False,
    },
    "8" : {"id":"8",
    "difficulty" : "Medium",
    "number": "4",
    "transcription": ".-.. .. --- -.",
    "audio_src": "somelink",
    "next_question": "9",
    "prev_question": "7",
    "question_type" : "english_morse",
    "word" : "LION",
    "answer" : ".-.. .. --- -.",
    "answered" : False,
    },
    "9" : {"id":"9",
    "difficulty" : "Medium",
    "number": "5",
    "transcription": ".-.. -.-- -.. .. .-",
    "audio_src": "somelink",
    "next_question": "end",
    "prev_question": "8",
    "question_type" : "english_morse",
    "word" : "LYDIA",
    "answer" : ".-.. -.-- -.. .. .-",
    "answered" : False,
    },
    "10" : {"id":"10",
    "difficulty" : "Hard",
    "number": "1",
    "transcription": "-.-. .- - -.-. .... ..--- ..---",
    "audio_src": "CATCH22.wav",
    "next_question": "11",
    "prev_question": "-1",
    "question_type" : "morse_english",
    "word" : "CATCH22",
    "answer" : "CATCH22",
    "answered" : False,
    },
    "11" : {"id":"11",
    "difficulty" : "Hard",
    "number": "2",
    "transcription": "..- .. -.. . ... .. --. -.",
    "audio_src": "UIDESIGN.wav",
    "next_question": "12",
    "prev_question": "10",
    "question_type" : "morse_english",
    "word" : "UIDESIGN",
    "answer" : "UIDESIGN",
    "answered" : False,
    },
     "12" : {"id":"12",
    "difficulty" : "Hard",
    "number": "3",
    "transcription": "----. ----. .--. .-. --- -... .-.. . -- ...",
    "audio_src": "99PROBLEMS.wav",
    "next_question": "13",
    "prev_question": "11",
    "question_type" : "sound_morse",
    "word" : "99PROBLEMS",
    "answer" : "----. ----. .--. .-. --- -... .-.. . -- ...",
    "answered" : False,
    },
    "13" : {"id":"13",
    "difficulty" : "Hard",
    "number": "4",
    "transcription": "..--- ----- ..--- ..---",
    "audio_src": "somelink",
    "next_question": "14",
    "prev_question": "12",
    "question_type" : "english_morse",
    "word" : "2022",
    "answer" : "..--- ----- ..--- ..---",
    "answered" : False,
    },
    "14" : {"id":"14",
    "difficulty" : "Hard",
    "number": "5",
    "transcription": "... .- -- ..- . .-.. / ..-. / -... / -- --- .-. ... .",
    "audio_src": "somelink",
    "next_question": "end",
    "prev_question": "13",
    "question_type" : "english_morse",
    "word" : "SAMUEL F B MORSE",
    "answer" : "... .- -- ..- . .-.. / ..-. / -... / -- --- .-. ... .",
    "answered" : False,
    },

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

@app.route('/learn_easy')
def easyLetters():
    global alphabet
    return render_template('letter_easy.html', data=alphabet)

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
    global score
    return render_template('quiz.html', question=question, score=score) 

@app.route('/quiz/end')
def end():
    global score
    global quiz_questions
    # reset score to 0 when you reach end page
    final_score = score
    score = 0
    for i in range(len(quiz_questions)):
        quiz_questions[str(i)]["answered"] = False
    return render_template('end.html', score=final_score) 

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
    global quiz_questions
    json_data = request.get_json()
    ans = json_data["answer"]
    qid = json_data["question_id"]
    correct = 0
    if(ans.lower() == quiz_questions[str(qid)]["answer"].lower()):
        correct = 1
    score += correct
    quiz_questions[str(qid)]["answered"] = True
    return jsonify(correct=correct)

@app.route('/not_implemented')
def not_implemented():
    return render_template('not_implemented.html')  


if __name__ == '__main__':
   app.run(debug = True)





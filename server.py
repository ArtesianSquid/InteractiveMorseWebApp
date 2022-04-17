from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

# ROUTES
@app.route('/')
def home():
    return render_template('home.html')  

@app.route('/learn/<id>')
def learn(id=None):
    return render_template('learn.html') 

@app.route('/quiz/<id>')
def quiz(id=None):
    return render_template('quiz.html') 

@app.route('/end')
def end():
    return render_template('end.html') 


# AJAX FUNCTIONS


if __name__ == '__main__':
   app.run(debug = True)





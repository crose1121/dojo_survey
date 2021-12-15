from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.model_file import Dojo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('results.html')


@app.route('/process', methods=['POST'])
def process():
    print(request.form['location'])
    if Dojo.validate_input(request.form):
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']

        return redirect('/result')
    else:
        return redirect('/')
from flask import Flask, render_template, redirect, url_for, request
import pandas as pd
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tables')
def tables():
    xlsx = pd.ExcelFile('google_survey_data.xlsx')
    excel_file = pd.read_excel(xlsx, 'Qual', index_col=[0, 1, 2])
    return render_template('tables.html', excel_file=excel_file)

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Credenciales invalidas, intente otra vez'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

if __name__=='__main__':
    app.run(debug=True, port=8000)
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os
import json
load_dotenv()
import nltk 

from nltk.sentiment.vader import SentimentIntensityAnalyzer

import pandas as pd
import numpy as np
import recom as rec
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity as distance

app = Flask(__name__)

# MySQL Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = os.getenv('SECRET_KEY')
app.config['MYSQL_DB'] = 'chats'

mysql = MySQL(app)

# settings
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM chats.chats')
    data = cur.fetchall()
    return render_template('index.html', users = data)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        userName = request.form['userName']
        text = request.form['text']
        idUser = request.form['idUser']
        idChat = request.form['idChat']
        idMessage = request.form['idMessage']
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO chats.chats 
                        (userName,text,idUser,idChat,idMessage) 
                        VALUES (%s,%s,%s,%s,%s)''',(userName,text,idUser,idChat,idMessage))
        mysql.connection.commit()
        flash('User Added Successfully')
        return redirect(url_for('index'))
        
@app.route('/edit/<string:idMessage>')
def get_user(idMessage):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM chats WHERE idMessage= {}'.format(idMessage))
    data = cur.fetchall()
    return render_template('add_user.html', user = data[0])

@app.route('/update/<string:idMessage>', methods = ['POST'])
def update(idMessage):
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        userName = request.form['userName']
        text = request.form['text']
        idUser = request.form['idUser']
        idChat = request.form['idChat']
        cur.execute(""" UPDATE chats
                        SET userName =%s,
                        text = %s,
                        idUser = %s,
                        idChat = %s
                        WHERE idMessage = %s    
        """,(userName,text,idUser,idChat,idMessage))
        mysql.connection.commit()
        flash('User Update Successfully')
        return redirect(url_for('index'))

@app.route('/delete/<string:idMessage>')
def delete_user(idMessage):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM chats WHERE idMessage = {}'.format(idMessage))
    mysql.connection.commit()
    flash('User removed Successfully')
    return redirect(url_for('index'))

@app.route('/analyze/<idChat>')
def analyze(idChat):
    sid = SentimentIntensityAnalyzer()
    cur = mysql.connection.cursor()
    cur.execute('SELECT text FROM chats WHERE idChat = {}'.format(idChat))
    analisis = cur.fetchall()
    data = json.dumps(analisis)
    text = str(data.encode('utf-8'))
    sent = sid.polarity_scores(text)
    return render_template('analyze.html', sent = sent)

@app.route('/sentiment/<idUser>')
def sentiment(idUser):
    sid = SentimentIntensityAnalyzer()
    cur = mysql.connection.cursor()
    cur.execute('SELECT text FROM chats WHERE idUser = {}'.format(idUser))
    analisis = cur.fetchall()
    data = json.dumps(analisis)
    text = str(data.encode('utf-8'))
    sent_user = sid.polarity_scores(text)
    return render_template('sentiment.html', sent = sent_user)

@app.route('/friendship/<name>')
def friendship(name):
    cur = mysql.connection.cursor()
    cur.execute('SELECT userName,text FROM chats.chats')
    data = cur.fetchall()
    df = pd.DataFrame(data)
    data = df.groupby(0)[1].apply(', '.join).reset_index()
    dicc = dict(zip(data[0], data[1]))
    friend = rec.recommender(name,dicc)
    data = json.dumps(friend)
    return render_template('friend.html', data = data)
    
    
if __name__ == '__main__':
    app.run(port = 8080, debug = True)
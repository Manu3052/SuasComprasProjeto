import os
import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

def db_connection():
    conn = psycopg2.connect(host="localhost",
                            dbname="Lista",
                            user="postgres",
                            password="manuele203")
    return conn

@app.route('/')
def index():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM lista_objetos;')
    lista = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', lista=lista)

#list table data
from logging import root
from unicodedata import name
from flask import Flask,  request, render_template
from db_config import get_db_connection
app=Flask("__name1__")

@app.route("/")
@app.route("/home")
def home():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM reviews;')
    data = cur.fetchall()
    print('data',data)
    conn.commit()

    cur.close()
    conn.close()
    return "hello  , this is home<h1>HELLO1</h1>"

    
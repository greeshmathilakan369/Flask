from logging import root
from unicodedata import name
from flask import Flask

app=Flask("__name1__")

@app.route("/")
def home():
    return "hello  , this is home<h1>HELLO1</h1>"


if __name__=="__main__":
 app.run(debug=True)
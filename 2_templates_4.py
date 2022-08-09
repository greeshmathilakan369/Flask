#use of layout...overriding..blockk content
#retrify pblm of 2_templates_3.py also.

from flask import Flask,render_template
from logging import root
from unicodedata import name


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

app=Flask("__name__")

@app.route("/")
@app.route("/home")
def home():
    return render_template('home4.html',posts=posts)
    

@app.route("/about")    
def about():
    return render_template('about4.html',title ='About')
    
if __name__=="__main__":
    app.run()
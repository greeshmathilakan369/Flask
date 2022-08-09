from flask import Flask,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
app=Flask("__name1__")

@app.route("/")
@app.route("/home")
def home():
    return "hello  , this is home<h1>HELLO1</h1>"

@app.route("/about")
def about():
    return "this is about page<h1>About</h1>"


if __name__=="__main__":
 app.run(debug=True)


app.config['SECRET_KEY']='5693658ffb333333'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite_site:///db'

db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    image_file=db.Column(db.String(20),unique=False,nullable=False)
    password=db.Column(db.String(20),nullable=False)
    posts=db.relationship('Post',backref=True,lazy=True)


    def __repr__(self):
        return f"User{'{self.username}','{self.password}','{self.image}'}"

class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)     
    content=db.Column(db.Text,nullable=False)   
    def __repr__(self):
        return f"Post{'{self.id}','{self.title}','{self.content}'}"
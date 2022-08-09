#workking and finished
from flask import Flask,render_template
from logging import root
from unicodedata import name

# posts=[
#     {'author':'corey MS',"Blog":"Post no1",'Title':'Google loon'},
#     {'author':'Jane cope','Blog':'Post no2','Title':'Genome Sequences'},
#     {'author':'martha gails','Blog':'post3'}
#     ]

app=Flask("__name__")

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')
    #  ,posts=posts)  

@app.route("/about")    
def about():
    return render_template('about.html')
    # ,posts=posts) 

if __name__=="__main__":
    app.run()


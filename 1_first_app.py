#flak basics and create basic routes
from crypt import methods
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
    return render_template("")

@app.route("/about")
def about():
    return "this is about page<h1>About</h1>"

@app.route('/reviews', methods =["GET", "POST"])
def review():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        review=request.form.get("review")
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO public.reviews (name, email, review)' 'VALUES(%s, %s, %s)', (name,email,review))
        conn.commit()
        cur.close()
        conn.close()
        return "Your name is "+name +"email is"+email+"review is"+review
    return render_template("post_data_new.html")



@app.route("/lists",methods=["GET","POST"])
def list():
    if request.method == "GET":
        list2 =[]
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM public.reviews")
        list2=cur.fetchall()
        print(list2,"staert")
        conn.commit()
        cur.close()
        conn.close()
        print(list2)
    return render_template("listdata.html",lists=list2)  

@app.route("/delete/<int:id>",methods=["GET","POST"]) 
def delete(id):
    if request.method=="GET":
        conn=get_db_connection()
        cur=conn.cursor()
        cur.execute("DELETE from public.reviews where id="+str(id)) 
        conn.commit()
        cur.close()
        conn.close()
    return "Sucessfully deleted" 


@app.route("/update",methods=["GET","POST"])
def update():
    if request.method=="POST":
        conn=get_db_connection()
        cur=conn.cursor()
        id=request.form.get("id")
        name=request.form.get("name")
        email=request.form.get("email")
        review=request.form.get("review")
        strSQl= "update public.reviews set name='"+name+"',email='"+email+"', review='"+review+"' where id="+str(id)
        cur.execute(strSQl)
        # data=cur.fetchall()
        # print("data................",data)
        conn.commit()
        cur.close()
        conn.close()
    return render_template("update.html") 
if __name__=="__main__":
 app.run(debug=True)
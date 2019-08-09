from flask import Flask, render_template ,request
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    # firstName = "Manish"
    # lastName = "Juriani"
    return render_template("index.html")


@app.route('/form')
def form():
    return render_template("form.html")

@app.route('/postUser',methods=['POST'])
def addUser():
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    contact = request.form['contact']
    email = request.form['email']
    return render_template("postUser.html",firstName=firstName,lastName=lastName,contact=contact,email=email)
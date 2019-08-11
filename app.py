# User __init__()
from flask import Flask, render_template , request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt
# from flask_msqldb import MySQL

# import mysql.connector
# from mysql.connector import Error, MySQLConnection
# from mysql.connector import (connection)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    from app import db
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(80), unique=False)
    lastName = db.Column(db.String(80), unique=False)
    email = db.Column(db.String(120), unique=False)
    contact = db.Column(db.String(13), unique=False)



    def __init__(self, firstName, lastName, email, contact):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.contact = contact
    
    def __repr(self):
        return '<User {}>'.format(self.firstName)

# @app.route('/index',methods=['GET'])
@app.route('/',methods=['GET','POST'])
def index():
    from app import db
    users = User.query.all()
    
    return render_template("index.html",users=users)


@app.route('/form')
def form():
    return render_template("form.html")

@app.route('/postUser',methods=['POST'])
def addUser():
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    email = request.form['email']
    contact = request.form['contact']
    from app import db    
    if firstName and lastName and contact and email:
        new_user = User(firstName=firstName,
                            lastName=lastName,
                            email=email,
                            contact=contact
                        )
        db.session.add(new_user)
        db.session.commit()
        users = User.query.all()
    
    return render_template("index.html",users=users)

@app.route('/<user_id>',methods=['GET','POST'])
def updateUser(user_id):
    from app import User
    from app import db
    
    updateData = User.query.filter_by(id=user_id).first()
    
    firstName = updateData.firstName     
    lastName = updateData.lastName
    email = updateData.email     
    contact = updateData.contact     
    
    # redirect(url_for('index'))
    return render_template("updateForm.html",id=user_id,firstName=firstName,lastName=lastName,email=email,contact=contact)

@app.route('/makeChanges/<user_id>',methods=['GET','POST'])
def makeChanges(user_id):
    from app import User
    from app import db
    updateData = User.query.filter_by(id=user_id).first()
    updateData.firstName = request.form['firstName']     
    updateData.lastName = request.form['lastName']
    updateData.email = request.form['email']
    updateData.contact = request.form['contact']
    db.session.commit()
    return redirect(url_for('index'))
    # users = User.query.all()

@app.route('/deleteUser/<user_id>',methods=['POST'])
def deleteUser(user_id):
    from app import User
    from app import db
    delete = User.query.filter_by(id=user_id).first()
    # delete = procedure_get_user_by_id(user_id)
    db.session.delete(delete)
    db.session.commit()
    users = User.query.all()
    return redirect(url_for('index'))
    # return render_template("index.html",users=users)

# def getConnection():
    # try:
    #     connection = mysql.connector.connect(host='localhost',
    #                                     database='users',
    #                                     user='root',
    #                                     password='1234')
    #     if cnx.is_connected():
    #         db_Info = cnx.get_server_info()
    #         print("Connected to MySQL database... MySQL server version on ",db_Info)

    #     return cnx
    # except Error as e:
    #     print("Error while connecting to the database", e)

    # try:
    #     cnx = connection.MySQLConnection(user='root', password='1234    ',
    #     host='127.0.0.1',
    #     database='users')
    #     return cnx
    # except Error as e:
    #     print("Error while connecting to database", e)

# def procedure_get_user_by_id(id):
#     # connection = getConnection()
#     try:
#         cnx = connection.MySQLConnection(user='root', password='1234',
#                                         host='127.0.0.1',
#                                         database='users')
#         # return cnx
#     except Error as e:
#         print("Error while connecting to database", e)
#     cursor = cnx.cursor()
#     cursor.callproc('get_user_by_id',id)
#     result = cursor.stored_results().fetchone()
    

#     if(cnx.is_connected()):
#         cursor.close()
#         cnx.close()
#         print("MySQL connection is closed")

#     return result
from pickle import GET, TRUE
from flask import Flask,render_template,request, session
import sqlite3 as sq
import random
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime





app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db'


db = SQLAlchemy(app)
#tables

class Customer(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(30))
    gender = db.Column(db.String(30))
    date = db.Column(db.Date)
    dr = db.Column(db.String(30))
    street = db.Column(db.String(30))
    city = db.Column(db.String(30))
    state = db.Column(db.String(30))

    def __init__(self,id,name,gender,date,dr,street,city,state):
        self.id = id
        self.name = name
        self.gender=gender
        self.date = date
        self.dr = dr
        self.street = street
        self.city = city
        self.state = state


class Authentiion_details(db.Model):
    email = db.Column(db.String(30),primary_key = True)
    password = db.Column(db.String(30))
    id = db.Column(db.Integer)
    def __init__(self,email,password,id):
        self.email = email
        self.password = password
        self.id = id

class Account(db.Model):
    acc_no = db.Column(db.Integer,primary_key = True)
    acc_type = db.Column(db.String(30))
    balance = db.Column(db.Integer,default = 0)
    id = db.Column(db.Integer)

    def __init__(self,acc_no,acc_type,balance,id):
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.balance = balance
        self.id = id

class Card(db.Model):
    card_no = db.Column(db.Integer,primary_key = True)
    card_type = db.Column(db.String(30))
    exp_date = db.Column(db.String(30))
    id = db.Column(db.Integer)

    def __init__(self,card_no,card_type,exp_date,id):
        self.card_no = card_no
        self.card_type = card_type
        self.exp_date = exp_date
        self.id = id

class Transactions(db.Model):
    T_id = db.Column(db.Integer,primary_key = True)
    acc_f = db.Column(db.Integer)
    acc_t = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    date = db.Column(db.Date)

@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/reg_customer",methods = ['POST', 'GET'])
def sign_up():
    if(request.method == "GET"):
        return render_template("signup.html")
    else:
        id = random.randint(1000000,9999999)
        name = request.form.get('name')
        gender = request.form.get('gender')
        dob = datetime.strptime(request.form.get('dob'),'%Y-%m-%d').date()
        dr = request.form.get('dr')
        street = request.form.get('street')
        city = request.form.get('city')
        state = request.form.get('state')
        email = request.form.get('email')
        password = request.form.get('password')
        cus = Customer(id,name,gender,dob,dr,street,city,state)
        aut = Authentiion_details(email,password,id)
        acc = Account(id,'Savings',0,id)
        card = Card(random.randint(1000000,9999999),'Debit','31-12-2030',id)
        db.session.add(cus)
        db.session.add(aut)
        db.session.add(acc)
        db.session.add(card)
        db.session.commit()
        return render_template("signup_success.html",c_id = id)

@app.route("/customer_login",methods = ['POST', 'GET'])
def cus_login():
    if request.method == 'GET':
        return render_template('customer_login.html')
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        #to get password
        conn = sq.connect('bank.db')
        cor = conn.cursor()
        cor.execute("SELECT * FROM authentiion_details WHERE email = ?",(email,))
        user = cor.fetchone()
        conn.commit()
        conn.close()
        if user[1] != password:
            return "wrong password"

        else:
            #to get id
            id = user[2]
            conn = sq.connect('bank.db')
            cor = conn.cursor()
            cor.execute("SELECT name FROM customer WHERE id = ?",(id,))
            name = cor.fetchone()
            conn.commit()
            conn.close()

            #to get accounts
            conn = sq.connect('bank.db')
            cor = conn.cursor()
            cor.execute("SELECT acc_no FROM account WHERE id = ?",(id,))
            accounts = cor.fetchall()
            conn.commit()
            conn.close()
            return render_template('dashboard_temp.html',id = id,name = name[0],accounts = accounts )

@app.route("/dashboard",methods = ['POST'])
def dashboard():
    acc_no = request.form.get('acc_no')
    acc_no = int(acc_no[1:-2])

    print(acc_no)
    #to get balance
    conn = sq.connect('bank.db')
    cor = conn.cursor()
    cor.execute("SELECT balance FROM account WHERE acc_no = ?",(acc_no,))
    bal = cor.fetchone()
    conn.commit()
    conn.close()

    #to get card details
    conn = sq.connect('bank.db')
    cor = conn.cursor()
    cor.execute("SELECT * FROM card WHERE id = ?",(acc_no,))
    cards = cor.fetchall()
    conn.commit()
    conn.close()


    return render_template('dashboard.html',bal = bal,cards = cards,acc_no = acc_no)
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
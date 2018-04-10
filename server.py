from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = 'durantula'
import re
from datetime import datetime
from time import time
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/results', methods=['POST'])
def process():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    bday = request.form['bday']
    print(bday)
    print(newBday)
    today = datetime.now()
    print(today)
    t1 = datetime.datetime.now()
    t2 = datetime.datetime.now()
    t1>t2



    password = request.form['password']
    confirm_password = request.form['confirm_password']

    #--------------------FIRST NAME VALIDATION--------------------------------------------
    # CHECK IF FIRST NAME FIELD IS EMPTY
    if len(first_name) < 1:
        flash(f'First name Cannot be empty')
        return redirect('/')
    # CHECK IF NAME CONTAINS A NUMBER
    def num_there(s):
        return any(i.isdigit() for i in s)
    if num_there(first_name) == True:
        flash(f'First name Cannot contain numbers')
    #---------------------LAST NAME VALIDATION--------------------------------------------
    # CHECK IF LAST NAME FIELD IS EMPTY
    if len(last_name) < 1:
        flash(f'last name Cannot be empty')
        return redirect('/')
    # CHECK IF LAST CONTAINS A NUMBER
    def num_there(s):
        return any(i.isdigit() for i in s)
    if num_there(last_name) == True:
        flash(f'Last name Cannot contain numbers')
    #---------------------EMAIL VALIDATION------------------------------------------------
    # CHECK IF EMAIL IF VALID
    if len(email) < 1:
        flash("Email cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    #-----------------------PASSWORD VALIDATION--------------------------------------------
    #CHECK IF IS VALID AND MATCHING
    if password != confirm_password:
        flash(f"Passwords do not match")
        return redirect('/')
    if len(password) < 8:
        flash(f"Password must contain at least 8 characters")
        return redirect('/')
    # CHECKS IF PASSWORD HAS AT LEAST 1 CHARACTER
    if not re.search(r"[\d]+", password):
        flash(f"Password must contain at least 1 numeric value")
        return redirect('/')
    # CHECKS FOR PASSWORD 1 UPPERCASE CHARACTER
    if not re.search(r"[\d]+", password):
        flash(f"Password must contain at least 1 uppercase character")
        return redirect('/')
    if not re.search(r"[A-Z]+", password):
        flash(f"Password must contain at least 1 uppercase character")
        return redirect('/')


    return render_template('results.html', first_name = first_name, last_name = last_name, email = email)
    # return redirect('/')
if __name__=="__main__":
    app.run(debug = True)   
from flask import Blueprint, render_template, request, redirect
from .db import users

# blueprints mean routes 

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("")

@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']

        # use regex to check email formats

        try:
            users.insert_one({"first_name": first_name,
                              "last_name": last_name,
                              "email": email,
                              "password": password
                            })
            return redirect("/")
        
        except Exception as e:
            return f"ERROR:{e}"
        
    else:
        return render_template("signup.html")
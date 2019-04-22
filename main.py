

from flask import Flask, request, redirect, render_template 
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/") 
def index():
   return render_template("signup.html")


@app.route("/validate_user", methods=["POST"])
def validate_user():
    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""
    
    if username == "":
        username_error="Username cannot be blank"

    if len(username) < 3:
        username_error = "Username must be between 3 and 20 characters" 
    
    if len(username) >20:
        username_error = "Username must be between 3 and 20 characters"
    
    if " " in username:
        username_error = "Spaces not allowed in username" 

    if password == "":
        password_error = "Password cannot be blank"
    
    if " " in password:
        password_error = "Spaces not allowed in password"
    
    if len(password) < 3:
        password_error = "Password must be between 3 and 20 characters" 
    
    if len(password) >20:
        password_error = "Password must be between 3 and 20 characters"

    if verify =="":
        verify_error = "Please enter password again"
     
    if " " in verify:
        verify_error = "Spaces not allowed in password"    
    
    if not password == verify:
        verify_error = "Passwords don't match"

    if not email =="":    
 
        if " " in email:
            email_error = "Spaces not allowed in email"       


        if len(email) <3:
            email_error = "Email must be between 3 and 20 characters" 

        if len(email) >20:
            email_error = "Email must be between 3 and 20 characters"    

        for char in email:
            if email.count ("@") < 1:
                email_error = "The email must contain an @ and a . to be valid"

            elif email.count ("@") > 1:
                email_error = "The email must contain an @ and a . to be valid"
            
            else:
                email_error=" "

    all_error_messages_combined = (username_error + password_error + verify_error + email_error)
    if all_error_messages_combined == "":
        return render_template("welcome.html",
            username=username)
    else:
        return render_template("signup.html", 
            username=username, 
            email=email, 
            email_error=email_error,
            username_error=username_error, 
            password_error=password_error,
            verify_error=verify_error)

app.run()




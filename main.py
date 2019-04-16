

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
        username_error="Username must be populated"

    if len(username) < 3:
        username_error = "User name must be longer than 3 and less than 20 characters" 
    
    if len(username) >20:
        username_error = "User name must be longer than 3 and less than 20 characters"
    
    if " " in username:
        username_error = "Spaces are not allowed in the username" 

    if password == "":
        password_error = "Password must be populated"
    
    if " " in password:
        password_error = "Spaces are not allowed in the password"
    
    if len(password) < 3:
        password_error = "User name must be longer than 3 and less than 20 characters" 
    
    if len(password) >20:
        password_error = "User name must be longer than 3 and less than 20 characters"

    if verify =="":
        verify_error = "Please enter password verification"
     
    if " " in verify:
        verify_error = "Spaces are not allowed in the password"    
    
    if not password == verify:
        verify_error = "Passwords don't match"

    if not email =="":    
 
        if " " in email:
            email_error = "Spaces are not allowed in the email"       


        if len(email) <3:
            email_error = "Email must be longer than 3 and less than 20 characters" 

        if len(email) >20:
            email_error = "Email must be longer than 3 and less than 20 characters"    

        for char in email:
            if email.count ("@") < 1:
                email_error = "The email must contain (1) @ and (1) . to be valid"

            elif email.count ("@") > 1:
                email_error = "The email must contain (1) @ and (1) . to be valid"
            
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




from flask import Flask, request, redirect
import string
import re

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            .error {{
                color: red;
            }}
        </style>
    </head>
    <body>
    <h1>Signup</h1>
        <form method="post">
            <table>
                <tr>
                    <td><label for="username">Username</label></td>
                    <td>
                        <input name="username" type="text" value= '{username}' >
                        <span class="error"> {username_error} </span>
                    </td>
                </tr>
                <tr>
                    <td><label for="password">Password</label></td>
                    <td>
                        <input name="password" type="password">
                        <span class="error">{empty_password}</span> 
                    </td>
                </tr>
                <tr>
                    <td><label for="verify">Verify Password</label></td>
                    <td>
                        <input name="verify" type="password">
                        <span class="error">{password_error}</span>
                    </td>
                </tr>
                <tr>
                    <td><label for="email">Email (optional)</label></td>
                    <td>
                        <input name="email" value='{email}'>
                        <span class="error">{email_error}</span>
                    </td>
                </tr>
            </table>
            <input type="submit">
        </form>
    </body>
</html>
"""



def isValidEmail(mail):
    if len(mail) > 3 and len(mail) < 20:
        if re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", mail) != None:
            return True
        else:
            return False
    else:
        return False

def usernameValidation(username):
    if len(username)<3 or len(username) >20 :
        return False
    else:
        for i in username:
            if i == " ":
                return False
        return True


@app.route("/")
def display_form():
    return form.format(username_error='',password_error='', email_error='', username = '', email = '', empty_password = '')

@app.route("/", methods=['POST'])
def validation():
    username = request.form['username']
    verify = request.form['verify']
    email = request.form['email']
    password = request.form['password']

    username_error =''
    password_error=''
    email_error=''
    empty_password=''

    if isValidEmail(email) == False or email == "":
        email_error = 'Not a valid email'
        email = ''
        

    if usernameValidation(username) == False or username == "":
        username_error = 'Not a valid username'
        username = ''

    

    if password == "":
        empty_password = "Enter your password!"
        password = ''
        verify = ''
    else: 
        if not password == verify:
            password_error = "Passwords don't match"
            password = ''
            verify = ''

    
    if not email_error and not username_error and not password_error and not empty_password:
        return "<h1>Welcome! " + username + "</h1>"
    else:
        return form.format(email_error=email_error, username_error=username_error, password_error=password_error, username = username, email = email, empty_password=empty_password)





app.run()
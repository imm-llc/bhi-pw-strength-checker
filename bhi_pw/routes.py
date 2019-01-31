from bhi_pw import app
from bhi_pw.hibp_api import pwndpw
from bhi_pw.best_practice_checker import main_func
from flask import render_template, request
import json, requests, binascii

@app.route('/', methods=["POST", "GET"])
def homepage():
    if request.method == "POST":
        password = request.form.get('Password')
        pwned_password_count = pwndpw.main_func(str(password))
        print(pwned_password_count)
        pwned_password_count = int(pwned_password_count)
        if pwned_password_count > 0:
            pwned_message = "Your password has been found in {} breaches".format(str(pwned_password_count))
        else:
            pwned_message = "This password was not found in any breaches"


        best_practice_match = main_func.check_best_practices(password)
        json_best_practice = json.loads(best_practice_match)
        
        best_practice_result = {}
        
        if json_best_practice['length'] == "ok":
            best_practice_result['length'] = "Your password is long. Great!"
        else:
            best_practice_result['length'] = "Your password is only {} characters. You should use a password that contains at least 10 characters".format(str(json_best_practice['pw_length']))
        
        if json_best_practice['uppercase'] == "bad":
            best_practice_result['uppercase'] = "You should include at least one upper case character in your password"
        else:
            best_practice_result['uppercase'] = "You have at least one uppercase character. Nice!"
        
        if json_best_practice['number'] == "bad":
            best_practice_result['number'] = "You should include at least one number in your password"
        else:
            best_practice_result['number'] = "You have at least one number in your password. Sweet!"
        
        if json_best_practice['special_char'] == "bad":
            best_practice_result['special_char'] = "You do not have a special character in your password. Special characters include: {}".format("@#$%^&*()_+=")
        else:
            best_practice_result['special_char'] = "You have a special character in your password. Awesome!"
        


        return render_template('result.html', breach_message=pwned_message, best_practice_result=best_practice_result)

    return render_template("home.html")

@app.route('/about', methods=["GET"])
def about():
    return "hello world"
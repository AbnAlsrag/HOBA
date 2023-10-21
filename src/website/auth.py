from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return render_template("logout.html")

@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password-1")
        password_confirm = request.form.get("password-2")

        if len(email) < 4:
            flash("Your email seems to be wrong type it again", category="error")
        elif password != password_confirm:
            flash("Your password doesn't match the confirmation password", category="error")
        elif len(password) < 4:
            flash("Your password it to short", category="error")
        else:
            flash("Account created!", category="success")

    return render_template("sign-up.html")
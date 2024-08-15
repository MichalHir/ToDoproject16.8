from flask import app, flash, redirect, render_template, request, url_for
from data import users, cards
from defs.prints import checks


@app.route("/signUp", methods=["GET", "POST"])
def signUp():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        newid = 1
        for user in users:
            if user["id"] == newid:
                newid += 1
        newuser = {
            "id": newid,
            "username": username,
            "password": password,
        }
        flash("sign up successful!", "success")
        users.append(newuser)
        # checks
        checks()
        return redirect("/")
    return render_template("signUp.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        checks()
        for user in users:
            if username == user["username"] and password == user["password"]:
                flash("Login successful!", "success")
                # checks

                # session.permanent = True
                # session["logged_in"] = True
                # session["username"] = username
                return redirect("/")
        # flash("not a valid username or password")
        return redirect("/login")
    return render_template("login.html")


@app.route("/logout")
def logout():
    # session.clear()
    flash("Goodbye. please login again soon")
    return redirect(url_for("login"))

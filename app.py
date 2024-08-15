from flask import Flask, flash, redirect, render_template, request, session, url_for

from side_defs.prints import checks

# from jinja2 import Template


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config["SESSION_PERMANENT"] = True
from data import users, cards


@app.route("/")
def main_page():
    # if not session.get("logged_in"):
    #     flash("please login", "danger")
    #     return redirect(url_for("login"))
    return render_template("main_page.html", users=users, cards=cards)


@app.route("/signUp", methods=["GET", "POST"])  # sign up works
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


@app.route("/logout")  # sign up works
def logout():
    # session.clear()
    flash("Goodbye. please login again soon")
    return redirect(url_for("login"))


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_card(id):
    for card in cards:
        if card["id"] == id:
            thiscard = card
        # flash("card edited successfully", "success")
    if request.method == "POST":
        for card in cards:
            if card["id"] == id:
                card["cardname"] = request.form.getlist("cardname")
                card["chores"] = request.form.getlist("chores")
        return redirect(url_for("main_page"))
    return render_template("edit.html", card=thiscard)


app.route("/add/<int:id>", methods=["GET", "POST"])


def add_card(id):
    for card in cards:
        if card["id"] == id:
            username = card["username"]
    if request.method == "POST":
        cardname = request.form.getlist("cardname")
        chores = request.form.getlist("chores")
        newid = 1
        for card in cards:
            if card["id"] == newid:
                newid += 1
        newcard = {
            "id": newid,
            "cardname": cardname,
            "username": username,
            "chores": chores,
        }
        cards.append(newcard)
        flash("card added successful!", "success")
        return redirect(url_for("main_page"))
    return render_template("add.html", username=username)


@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete_card(id):
    for card in cards:
        if card["id"] == id:
            # flash("Card deleted successfully", "success")
            cards.remove(card)
    # return redirect(url_for("main_page"))
    return render_template("main_page.html", users=users, cards=cards)


@app.route("/single/<string:username>", methods=["GET", "POST"])
def single(username):
    return render_template(
        "single.html", users=users, cards=cards, thisusername=username
    )


if __name__ == "__main__":
    app.run(debug=True)

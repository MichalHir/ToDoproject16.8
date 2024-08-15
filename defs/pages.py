from flask import app, render_template
from data import users, cards


@app.route("/")
def main_page():
    # if not session.get("logged_in"):
    #     flash("please login", "danger")
    #     return redirect(url_for("login"))
    return render_template("main_page.html", users=users, cards=cards)


@app.route("/single/<string:username>", methods=["GET", "POST"])
def single(username):
    return render_template(
        "single.html", users=users, cards=cards, thisusername=username
    )


@app.route("/single_card/<int:id>", methods=["GET", "POST"])  
def single_card(id):
    return render_template("single_card.html", cards=cards, id_number=id)

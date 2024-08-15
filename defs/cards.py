from flask import app, flash, redirect, render_template, request, url_for
from data import users, cards


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

from flask import Flask, render_template

# from jinja2 import Template


app = Flask(__name__)
from data import client, to_do


@app.route("/")
def main_page():
    return render_template('main_page.html', client=client)


if __name__ == "__main__":
    app.run(debug=True)

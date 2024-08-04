from flask import Flask, flash, redirect, render_template, request

# from jinja2 import Template


app = Flask(__name__)
from data import client, to_do


@app.route("/")
def main_page():
    return render_template('main_page.html', client=client)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        list=[]
    flash('Login successful!', 'success')

    return redirect('/')
return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)

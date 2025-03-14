import json
from flask import Flask, render_template, request, url_for
from pprint import pprint

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("regestr.html")

@app.route("/user", methods=["POST"])
def user():
    users = []
    with open("db/users.json", "r", encoding="utf-8") as f:
        users = json.loads(f.read())
        print((request.form))
    if request.form['username'] == 'admin':
        return render_template("regestr.html", error="This username is not available, please try another")
    else:
        return render_template("user.html", username=request.form['username'])

if __name__ == "__main__":
    app.run(debug=True)
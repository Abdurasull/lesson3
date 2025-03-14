from pprint import pprint
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
        # print((filter(lambda user: user['email'] == request.form['email'], users )))
        x = list(filter(lambda user: user['email'] == request.form['email'], users ))
        print(len(x) == 0)
        pprint(type(len(list(x))))
        print(request.form['email'])
        if len(x) == 0:
            users.append(request.form)
            pprint(users)
            with open("db/users.json", "w", encoding="utf-8") as f:
                f.write(json.dumps(users, indent=4, ensure_ascii=False))
            return render_template("index.html")    
            # print(users)
        else:
            return render_template("regestr.html", error="Bu email da foydalanuvchi ruyxatdan o`tgan, iltimos bosh email orqali urunib ko`ring")

if __name__ == "__main__":
    app.run(debug=True)
from pprint import pprint
import json
from flask import Flask, render_template, request, url_for
from pprint import pprint

app = Flask(__name__)

@app.route("/", endpoint="ok")
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
        
        x = list(filter(lambda user: user['email'] == request.form['email'], users ))
        if request.form['password'] == request.form['repate_password']:            
            if len(x) == 0:
                users.append(request.form)
            
                with open("db/users.json", "w", encoding="utf-8") as f:
                    f.write(json.dumps(users, indent=4, ensure_ascii=False))
                return render_template("user.html", user=request.form)    
                # print(users)
            else:
                return render_template("regestr.html", error="Bu email da foydalanuvchi ruyxatdan o`tgan, iltimos boshqa email orqali urunib ko`ring")
        else:
            return render_template("regestr.html", error="Parollar mos emas")


@app.route("/user_log", methods=["POST"])
def user_log():
    users = []
    with open("db/users.json", "r", encoding="utf-8") as f:
        users = json.loads(f.read())
        
        x_email = list(filter(lambda user: user['email'] == request.form['email'], users ))

        if len(x_email) and (x_email[0]['password']  == request.form['password']):
            return render_template("user.html", user=x_email[0])    
            # print(users)
        else:
            return render_template("login.html", error="Email yoki parol xato")
    

if __name__ == "__main__":
    app.run(debug=True)
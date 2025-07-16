from flask import Flask,render_template,request
import os
app=Flask(__name__)



@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not os.path.exists("users.txt"):
            with open("users.txt", "w") as f:
                pass  # Just create the file
        
        # Check if user already exists
        with open("users.txt", "r") as f:
            for line in f:
                existing_user, _ = line.strip().split("|")
                if existing_user == username:
                    return "User already exists. Try signing in."

        with open("users.txt", "a") as f:
            f.write(f"{username}|{password}\n")
        return "Signup successful! <a href='/signin'>Sign in</a>"

    return render_template("signup.html")

@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        with open("users.txt", "r") as f:
            for line in f:
                existing_user, existing_pass = line.strip().split("|")
                if existing_user == username and existing_pass == password:
                    session["username"] = username
                    return redirect("/")  # or redirect to order page

        return "Invalid credentials. Try again."

    return render_template("signin.html")

@app.route("/signout")
def signout():
    session.pop("username", None)
    return redirect("/")
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/order",methods=["GET","POST"])
def order():
    if request.method=="POST":
        name=request.form["name"]
        adress=request.form["adress"]
        medicine=request.form["medicine"]
        with open("orders.txt","a")as f:
            f.write(f"{name} | {adress} | {medicine}\n")
        return f"thank you {name},your medicine '{medicine}' will be delivered via drone"
    return render_template("order.html")
@app.route("/contact") 
def contact():
    return render_template("contact.html")
if __name__=="__main__":
    app.run(debug=True)

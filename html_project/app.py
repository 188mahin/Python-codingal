from flask import Flask, render_template, request, redirect, session
import os

app = Flask(__name__)
app.secret_key = "mahin"  


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not os.path.exists("users.txt"):
            with open("users.txt", "w") as f:
                pass

        with open("users.txt", "r") as f:
            for line in f:
                existing_user, _ = line.strip().split("|")
                if existing_user == username:
                    return "User already exists. Try signing in."

        with open("users.txt", "a") as f:
            f.write(f"{username}|{password}\n")

        session["username"] = username
        session["cart"] = []
        return redirect("/")

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
                    session["cart"] = []
                    return redirect("/")
        return "Invalid credentials. Try again."

    return render_template("signin.html")


@app.route("/signout")
def signout():
    session.pop("username", None)
    session.pop("cart", None)
    return redirect("/")


@app.route("/")
def home():
    if "username" not in session:
        return redirect("/signin")
    return render_template("home.html")


@app.route("/order", methods=["GET", "POST"])
def order():
    if "username" not in session:
        return redirect("/signin")

    if request.method == "POST":
        name = request.form["name"]
        address = request.form["address"]
        medicine = request.form["medicine"]
        with open("orders.txt", "a") as f:
            f.write(f"{name} | {address} | {medicine}\n")
        return f"Thank you {name}, your medicine '{medicine}' will be delivered via drone"
    
    return render_template("order.html")


@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    if "username" not in session:
        return redirect("/signin")

    medicine = request.form.get("medicine")
    if medicine:
        cart = session.get("cart", [])
        cart.append(medicine)
        session["cart"] = cart
    return redirect("/cart")


@app.route("/cart")
def cart():
    if "username" not in session:
        return redirect("/signin")

    cart_items = session.get("cart", [])
    return render_template("cart.html", cart=cart_items)
@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    if "username" not in session:
        return redirect("/signin")

    cart_items = session.get("cart", [])
    if request.method == "POST":
        name = request.form["name"]
        address = request.form["address"]
        with open("orders.txt", "a") as f:
            for item in cart_items:
                f.write(f"{name} | {address} | {item}\n")
        session["cart"] = []
        return f"Thank you {name}, your medicines will be delivered!"

    return render_template("checkout.html", cart=cart_items)


@app.route("/contact")
def contact():
    if "username" not in session:
        return redirect("/signin")
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
